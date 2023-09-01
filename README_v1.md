## ETL Pipeline 
Week 9 Project in WAIA Data Engineering Bootcamp

## Introduction 

Building an ETL pipeline that performs the follwing tasks: 
- Extract data of +400K invoices from Redshift 
- Transform the data by:
  - Remove Nulls
  - Remove corrupt stock codes
  - Fix column types
  - Remove duplicates

- Load the transformed data to an S3 bucket 

### Requirements 
- Python 3

### Instructions on how to excute the code
Make sure you are executing the code from designated folder
1. Install all the libraries you will need

    `` pip install -r requirements.txt
``


2. fill your credentials and enviroment variables into a .env


3. Run main.py script
  
   ``
   python3 main.py``

                
