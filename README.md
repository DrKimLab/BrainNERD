[![Language](https://img.shields.io/badge/Location-YaleNeurology-00356b.svg)](https://medicine.yale.edu/neurology/) [![Language](https://img.shields.io/badge/Lab-Dr.Kim-69d84f.svg)](https://medicine.yale.edu/lab/kim/) [![Language](https://img.shields.io/badge/Publisher-JamaOpenNetwork-FF3390.svg)](https://jamanetwork.com/journals/jamanetworkopen) [![Language Unix](https://img.shields.io/badge/Status-READY-<COLOR>.svg)]() [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1x7Kul4J4rYuIdlEuR8QRgtxzN6IXXHjg?usp=sharing) 




<center><h1> Development and Validation of a Model to Identify Critical Brain Injuries Using Natural Languege Processing of Text Computed Tomography Reports </h1></center>



**This project was develop by Dr. Kim Lab**
https://medicine.yale.edu/lab/kim/

**Paper source**
https://jamanetwork.com/journals/jamanetworkopen



# Table of contents
1. [Introduction](#introduction)
2. [Requirements](#paragraph1)
3. [Installation and How to use the Model](#paragraph2)
    1. [Installation](#subparagraph1)
    2. [Loading the Model](#subparagraph2)
    3. [Using Jupiter Notebooks](#subparagraph3)
    4. [Google Colab](#subparagraph4)

4. [Decoder Model](#paragraph4)
5. [Citation](#paragraph5)


## Introduction <a name="introduction"></a>
Clinical text reports from computed tomography(CT) represent rich, incompletely utilized information regarding acute brain injuries and neurologic outcomes. CT reports are unstructured; thus, extracting information at scare requires automated natural language processing (NLP). However, designing a new NLP algorithm for each individual category is an unwieldy proposition. An NLP tool that summarizes all injuries in head CT reports would facilitate the exploration of large data sets for clinical significance of neuroradiological findings.

## Requirements <a name="paragraph1"></a>
***Anaconda or Miniconda Environments*** https://docs.conda.io/en/latest/miniconda.html <br> 
***Python 3.7 or later***. https://www.python.org/ or  https://www.python.org/downloads/release/python-379/ <br> 
***Spacy 3.0***  https://spacy.io/ ( The model can work in newer versions of spacy, it would raise a warning, we would retrain the model in the newer versions) 

## Installation and How to use the Model <a name="paragraph2"></a>


### Installation <a name="subparagraph1"></a>
How to Create a new environment: <br>
In your Anaconda cmd enter: <br>
```
conda create -n Bner python=3.7  
conda activate Bner 
conda install -c conda-forge spacy 
conda install -c conda-forge cupy  
``` 

### Loading and or Downloading the Model <a name="subparagraph2"></a>
Inside the Models folder you will find the link to download the models. In order to use a model you need to save the model in your project directory. Or you can save the model in another directory and call the model directory from the load function <br>
Below is the link to download the model from our drive: <br>
https://drive.google.com/drive/folders/1iO3qA9XppRrnOqZWrrDyWXuIVpr7FzEJ?usp=sharing


### Using Jupiter Notebooks <a name="subparagraph3"></a>
Inside the Examples folder you will find few examples on how to use the model using jupyter notebooks. More examples to come**

### Google Colab <a name="subparagraph4"></a>
The link below will take you to a interactive tutorial on how to use the model. We will have many more tutorials soon. <br>

https://colab.research.google.com/drive/1x7Kul4J4rYuIdlEuR8QRgtxzN6IXXHjg?usp=sharing

## Decoder <a name="paragraph4"></a>
Here is a link for the Decoder model

## Citation <a name="paragraph5"></a>
If you use the model in your publications, please cite this Paper:



