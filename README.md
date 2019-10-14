# Python scikit-image (90 minutes)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/uschmidt83/neubias-ts13/master)

As the name suggests, this session will be about demonstrating how 
typical image processing and analysis tasks can be accomplished with 
[scikit-image](https://scikit-image.org/). I will prepare examples that I think are relevant, but this session could be more interactive based on the interests of the participants.


# Machine Learning (120 minutes)

We will first cover some machine learning (ML) basics and discuss the tradeoffs between traditional image analysis approaches and ML-based ones.
This session will focus on the tasks of image restoration and segmentation, for which we'll explore classic machine learning methods, as well as recent approaches based on deep learning (e.g. [CARE](http://csbdeep.bioimagecomputing.com), [StarDist](https://github.com/mpicbg-csbd/stardist)).
Examples will be demonstrated via Jupyter notebooks using Python, which you can follow along if you install the necessary software.


# Homework

Please install [Anaconda](https://www.anaconda.com/distribution/) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html), then make a new environment (here called `ts13`) and install the necessary packages, e.g. like this:

```console
$ conda create --name ts13 python=3.6
$ conda activate ts13
$ conda install numpy ipython jupyter matplotlib pandas scipy scikit-image scikit-learn seaborn tqdm
$ pip install matplotlib-scalebar
```

## Deep Learning

*I'll look into getting the deep learning examples to run on [Google Colab](https://colab.research.google.com), but can't promise that it'll work.*

If you want to follow along the deep learning examples on your own computer, please first [install TensorFlow 1.x](https://www.tensorflow.org/install) (**not TensorFlow 2**) by following the official instructions.

It is strongly recommended to use TensorFlow with [GPU support](https://www.tensorflow.org/install/gpu) if you have a compatible GPU from Nvidia. Note that it is very important to install the specific versions of CUDA and cuDNN that are compatible with the respective version of TensorFlow.

The packages for [Content-aware Image Restoration (CARE)](http://csbdeep.bioimagecomputing.com) and [StarDist - Object Detection with Star-convex Shapes](https://github.com/mpicbg-csbd/stardist) can then be installed with `pip`:

```console
$ pip install csbdeep
$ pip install stardist
```

Note that the `stardist` package relies on a C++ extension, which needs a suitable compiler to be installed on your system. Please read [this](https://github.com/mpicbg-csbd/stardist/blob/master/README.md#troubleshooting)
if you run into compilation problems.

If time permits, we'll also cover [Noise2Void - Learning Denoising from Single Noisy Images](https://github.com/juglab/n2v). Please install it like this:

```console
$ pip install git+https://github.com/juglab/n2v.git@master
```
