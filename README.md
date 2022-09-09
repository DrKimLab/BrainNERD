[![Language](https://img.shields.io/badge/Location-YaleNeurology-00356b.svg)](https://medicine.yale.edu/neurology/) [![Language](https://img.shields.io/badge/Lab-Dr.Kim-69d84f.svg)](https://medicine.yale.edu/lab/kim/) [![Language](https://img.shields.io/badge/Publisher-JamaOpenNetwork-FF3390.svg)](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2795179) [![Language Unix](https://img.shields.io/badge/Status-READY-<COLOR>.svg)]() [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1x7Kul4J4rYuIdlEuR8QRgtxzN6IXXHjg?usp=sharing) 




<center><h1> Development and Validation of a Model to Identify Critical Brain Injuries Using Natural Languege Processing of Text Computed Tomography Reports </h1></center>



**This project was develop by Dr. Kim Lab**
https://medicine.yale.edu/lab/kim/

**Paper source**
https://jamanetwork.com/journals/jamanetworkopen



# Table of contents
1. [Introduction](#introduction)
2. [Requirements for the NER Model](#paragraph1)
3. [Installation and how to use the NER Model](#paragraph2)
    1. [Installation](#subparagraph1)
    2. [Loading the Model](#subparagraph2)
    3. [Using Jupiter Notebooks](#subparagraph3)
    4. [Google Colab](#subparagraph4)

4. [Decoder Model](#paragraph3)
    1. [Introduction](#subparagraph5)
    2. [Reports](#subparagraph6)
    3. [BrainNERD.py](#subparagraph7)
    4. [PropertyExtraction.py](#subparagraph8)
    5. [Running this project - Files needed](#subparagraph9)
    6. [Running this project - Files needed](#subparagraph10) 
    7. [Running Database queries](#subparagraph11)

5. [Citation](#paragraph5)


## Introduction <a name="introduction"></a>
Clinical text reports from computed tomography(CT) represent rich, incompletely utilized information regarding acute brain injuries and neurologic outcomes. CT reports are unstructured; thus, extracting information at scare requires automated natural language processing (NLP). However, designing a new NLP algorithm for each individual category is an unwieldy proposition. An NLP tool that summarizes all injuries in head CT reports would facilitate the exploration of large data sets for clinical significance of neuroradiological findings.

## Requirements for the NER Model <a name="paragraph1"></a>
***Anaconda or Miniconda Environments*** https://docs.conda.io/en/latest/miniconda.html <br> 
***Python 3.7 or later***. https://www.python.org/ or  https://www.python.org/downloads/release/python-379/ <br> 
***Spacy 3.0***  https://spacy.io/ ( The model can work in newer versions of spacy, it would raise a warning, we would retrain the model in the newer versions) 

## Installation and How to use the NER Model <a name="paragraph2"></a>


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

# Decoder <a name="paragraph3"></a>

## Introduction <a name="subparagraph5"></a>
This project seeks to execute term tagging to represent CT reports as a mapping of
important terms to their presence in the document.


| Meaning | What to place in cell |
| ------- | -------|
| Pertinent positive - Term is mentioned specifically as being present in patient | + |
| Pertinent negative - Term is mentioned specifically as not present in patient   | - |
| Not mentioned - Term is not mentioned                                           | 0 |
| Possible - Term is mentioned with some uncertainty as to presence               | P |


## Reports <a name="subparagraph6"></a>
Reports are the long data output from our entity recognition model run on each document.
They are saved in this repo under /Long_data_manuscript or you can update the directory
in constants.py

These reports are CSV files with the following headers:
Term number,Entities,val

## BrainNERD.py <a name="subparagraph7"></a>
This is the script which runs our term tagging algorithm and checks its performance
against the provided validation file. Additionally, it will create data.sql with
the sql database representing the output as well as executes the queries outlined in /queries folder.

## PropertyExtraction.py <a name="subparagraph8"></a>
This is the script which runs our term tagging algorithm as well as property extraction. Additionally, it creates a database file named properties.sql as well as executes the queries outlined in /queries folder.

## Running this project - Files needed <a name="subparagraph9"></a>
When running you need the following files:
BrainNERD.py
constants.py
db.py
dbqueries.py
metrics.py
propertyExtraction.py
terms
validation/
  validation_final.csv
Long_data_manuscript/
  training/
    long_1.csv
    ...
  test/
    long_101.csv
    ...

## Running this project <a name="subparagraph10"></a>
#### Install python3: https://www.python.org/downloads/
#### Then run the following commands from your terminal while in this repo. Setup your virtual environment (only need to do once)
```
python3 -m venv brain
source brain/bin/activate
pip install sklearn
pip install tabulate

```

#### Make sure you are in your virtual environment (you should see (brain) to the left of your terminal) If you are not in your virtual environment, start by running:
```
source brain/bin/activate
```

#### Before running, make sure you edit the values in constants.py to point to your data, validation, etc.
- TERM_FILE
- LONG_DIR
- VALIDATION_DIR
- START_NUM
- DOC_COUNT
```
python BrainNERD.py
```

# Running Database queries <a name="subparagraph11"></a>
#### We have built in a method for running queries against the created Database. Start by creating a file in the /queries folder lets say query1.txt
#### Input an injury term followed by (+, -, or p) to denote whether you want to query for that term as present, not present, or possible. Each of these query parameters will be joined by an AND in the code. The file may look like below, which would mean to return all documents which have:
#### Hemmorhage present AND stroke not present AND hydrocephalus not present.
```
Hemorrhage +
Stroke -
Hydrocephalus -
```

### Option 1, Document summary and Aggregate info
#### Then simply run either the BrainNERD.py for just summary info. This will output into folder /queries-output. This error can be disregarded "The error 'UNIQUE constraint failed: documents.id' occurred"
```
python BrainNERD.py
```

#### Option 1 will yield one file:
- query1-output.txt:  contains the document summary and aggregate information of each injury.

### Option 2, Document summaries and injury property information
#### Or run propertyExtraction.py for injury property info as well. This will output into folder /queries-output-properties. This error can be disregarded "The error 'UNIQUE constraint failed: documents.id' occurred"
```
python propertyExtraction.py
```

#### Option 2 will yield two files:
- query1-doc.csv: contains the document summary for the documents which match your query
- query1-injury.csv: contains all of the properties related to all injuries in the document which matches your query.
#### Both of these files can be imported into excel for easier viewing.


### Running Datebase Queries (Manual)
#### Install Sqlite: https://www.tutorialspoint.com/sqlite/sqlite_installation.htm
#### Run the following commands to enter the sqlite terminal, load the output from brainclass, and set some settings. The final command will show you how the table was created and all of the column names.
```
sqlite3 data.sql
.headers ON
.mode column
.schema documents
```

### Useful templates for DB queries
#### Get all the data from the table
```
select * from documents;
```
#### Get document IDs according to some constraints. Notice that the last constraint is in parentheses to mean that stroke is either negative or not mentioned.
```
select id from documents WHERE Hemorrhage = "+" AND Edema = "p" AND (Stroke = "-" OR Stroke = "0");
```
#### Count number of documents where some constraint is true
```
select count(*) from documents WHERE Hemorrhage = "+" AND Edema = "p" AND (Stroke = "-" OR Stroke = "0");
```

## Citation <a name="paragraph5"></a>
If you use the model in your publications, please cite this Paper:
https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2795179



