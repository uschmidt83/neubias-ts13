#!/usr/bin/env python

import argparse
import sys

import numpy as np
from tqdm import tqdm
from pathlib import Path
import pandas as pd

# from pprint import pprint
# import matplotlib.pyplot as plt

from skimage.io import imread
from skimage.filters import thresholding
from skimage.measure import regionprops
from scipy.ndimage import label


description = """
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""


def parse_args():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter, description=description)

    data = parser.add_argument_group("input")
    data.add_argument('--input-dir',     type=str, required=True,  default=None,     help="path to folder with input images")
    data.add_argument('--input-pattern', type=str, required=False, default='*.tif*', help="glob-style file name pattern of input images")

    model = parser.add_argument_group("algorithm")
    model.add_argument('--threshold-value',  type=float, required=False, default=None,   help="intensity threshold value (to be used instead of automatic method)")
    model.add_argument('--threshold-method', type=str,   required=False, default='otsu', help="automatic thresholding method", choices=['isodata','li','mean','minimum','otsu','triangle','yen'])

    output = parser.add_argument_group("output")
    output.add_argument('--output-file', type=str, required=False, default='measurements.csv',         help="path to file where results (as CSV) will be save")
    output.add_argument('--dry-run',               required=False, default=False, action='store_true', help="do a dry run, i.e. don't save results to disk")

    return parser.parse_args()


def process(args):
    # pprint(vars(args))

    # get list of input files and exit if there are none
    file_list = list(Path(args.input_dir).glob(args.input_pattern))
    if len(file_list) == 0:
        print("No files to process in '%s' with pattern '%s'." % (args.input_dir,args.input_pattern))
        sys.exit(0)

    get_threshold = eval(f"thresholding.threshold_{args.threshold_method}")

    measurements = {}

    for f in tqdm(file_list):
        img = imread(str(f))

        thresholded = img > get_threshold(img)
        segmented = label(thresholded)[0]
        regions = regionprops(segmented)
        areas = [r.area for r in regions]

        measurements.setdefault('objects found',[]).append(len(regions))
        measurements.setdefault('area (mean)',[]).append(np.mean(areas))
        measurements.setdefault('area (std)',[]).append(np.std(areas))

    df = pd.DataFrame(measurements, index=[f.name for f in file_list])
    if not args.dry_run:
        print(f"{'overwriting' if Path(args.output_file).exists() else 'saving'} '{args.output_file}'")
        df.to_csv(str(args.output_file))

    # display(df)



if __name__ == '__main__':
    if not ('__file__' in locals() or '__file__' in globals()):
        print('running interactively, exiting.')
        sys.exit(0)

    # parse arguments
    args = parse_args()

    # execute workflow
    process(args)
