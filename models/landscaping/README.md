# Purpose
Patent landscaping is the process of finding patents related to a particular topic. It is important for companies, investors, governments, and academics seeking to gauge innovation and assess risk. However, there is no broadly recognized best approach to landscaping. Frequently, patent landscaping is a bespoke human-driven process that relies heavily on complex queries over bibliographic patent databases. In this paper (and repository), we present Automated Patent Landscaping, an approach that jointly leverages human domain expertise, heuristics based on patent metadata, and machine learning to generate high-quality patent landscapes with minimal effort.

# Creating a Patent Landscape

The figure 1 shows the high level flow to create a patent landscape. We'll walk through each of these in turn in the accompanying Jupyter Notebook.

![Fig 1. High Level Flow of Automated Patent Landscaping](figs/flow.png)

## Requirements
Before we get started, you should install some requirements for running this notebook. We rely on TensorFlow, Keras, and Google's Cloud infrastructure such as BigQuery, where we pull public patent data, and that needs to be installed and authorized. You need a few basics before continuing:
* Anaconda
* Jupyter Notebooks
* TensorFlow and Keras
* Google Cloud SDK
* BigQuery Python Client
* A few Python utilities

### Platform Support

Note that this has primarily been tested using Linux (Ubuntu) and Windows 10
with both CPU-based TensorFlow and with GPUs. There's no reason this shouldn't
work just fine with MacOS, but it's not been thoroughly tested. If you encounter
issues with the instructions, please feel free to reach out to
[Dave Feltenberger](https://github.com/seinberg) or send a pull request with a fix.

### Anaconda
I strongly recommend using Anaconda for this - it helps manage environments for Python, and these instructions will assume you're using it. Download Anaconda from [https://www.anaconda.com/download/](https://www.anaconda.com/download/). Install the Python 3.6 version, *not* 2.7.

Once Anaconda is installed, create an environment:
```
conda create -n patent-landscape python=3.5
source activate patent-landscape (or just: activate patent-landscape if you're in Windows)
```

### Jupyter Notebooks

To run the code in this notebook, you'll also need to install Jupyter. The following installs Jupyter and some utilities that let you toggle between different conda environments while inside a notebook.

```
conda config --add channels conda-forge
conda install jupyter ipython nb_conda=2.2.0
```

### Installing pip

Some packages we depend on use `pip` for package management. If you're in Windows or Linux, installing Anaconda should take care of this for you. If you're on a Mac, there's a chance this isn't installed and that you need to install it yourself. You can install it with this command:
```
conda install pip
```

### TensorFlow and Keras

TensorFlow will work 'out of the box' with just your CPU. Since we're going to be building a model using neural networks, however, I highly recommend using GPU acceleration - training will be at least an order of magnitude faster with a modern GPU. You'll need to follow the TensorFlow instructions found [here](https://www.tensorflow.org/install/) for your platform. There are several steps to getting your GPU working for Deep Learning, so pay careful attention to the instructions. Note that only Nvidia chipset-based GPUs will work with TensorFlow.

To skip all the GPU acceleration and just get started, you can just run this command within your active conda environment:
```
pip install tensorflow
```

Keras is an excellent high level Deep Learning library that we'll use to build our models:
```
conda install keras
```

Also install tflearn, the high-level library on top of TensorFlow, if you'd like to experiment with another high-level library like Keras (though our example doesn't directly use tflearn):
```
pip install tflearn
```

### Google Cloud SDK
***Download and install Google Cloud SDK.*** You can download and install using [these](https://cloud.google.com/sdk/docs) instructions. On Linux, you'll need to source the `.sh` file and source the relevant include files to make sure the binaries are in your path. You should also install the python utilities for your Anaconda project:

```
pip install google-cloud
pip install google-cloud-storage
```

Once you have the `gcloud` client installed, you need to authorize it to access Google's Cloud on your behalf. ***Don't forget this, or you'll get difficult to debug errors while running the code!*** From your active conda environment, run this command and follow the prompts:
```
gcloud auth application-default login
```

Finally, you'll also need to install the Google API Python Client and BigQuery extension to Pandas:
```
pip install google-api-python-client pandas-gbq
```

### Python Utilities

```
conda install numpy pandas h5py scipy scikit-learn matplotlib seaborn
```

## Google Cloud Tools Client Authorization

For this code to run properly, you need to authorize Google Cloud to run. This is important or you'll get weird errors that are hard to debug :) See above, the `gcloud` command.

# Running the Landscaping Code

There are two primary steps: 1) cloning the Github repo, and 2) starting
Jupyter.

## 1) Clone the Landscaping Github Repo

```
git clone https://github.com/google/patents-public-data
```


## 2) Start Jupyter

Now that you have the Repo, from a command line, change into the root of the
repository you just cloned. The Jupyter notebook we care about is in
`models/landscaping/LandscapeNotebook.ipynb`. Finally, set an environment
variable and start Jupyter:

```
export KERAS_BACKEND=tensorflow; jupyter notebook
```

*Note*: don't forget to change Conda environments to the patent-landscape one.
You can do this before starting `jupyter` with the following command:
```
source activate patent-landscape (or just: activate patent-landscape if you're in Windows)
```

or, once you're in the Jupyter environment, and assuming you've installed all
the packages mentioned above, by choosing the Environment menu option and
selecting the `patent-landscape` environment.
