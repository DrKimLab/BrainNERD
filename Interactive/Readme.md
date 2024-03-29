# Brainerd Interactive APP

Interactive Application for BrainNerd


### Instructions

*Create a new environment*

` conda create -n Brainnerd python=3.10.5`

`conda activate Brainnerd`

`pip install streamlit==1.22.0`

`pip install pandas==1.4.3`

`pip install spacy==3.4.1`

`pip install transformers==4.21.23`


### How to run the files 

- cd into the directory in where the Brainner Main file lives = Brainnerd.py

- excetucte the file

> - `streamlit run Brainnerd.py`


### The file structure should be like this:

```
Brainnerd/
│   │
|   Brainnerd.py
│   └───pages/
│       │   __init__.py
│       │   1_📑_Entity_Extraction_Findings.py
│       │   2_📝_Entity_Extraction_Complete_CT.py
│       │   3_📊_Tabular_Data_Extraction.py
│       │   4_📈_Entity_Visualization.py
│       │   5_🎯_Report_De_Identification_Model.py
|       |   model *The model needs to be stored in this folder*
```
