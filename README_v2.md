# ETL Pipeline v2 : Docker 

## Introduction 

Building an ETL pipeline that performs the follwing tasks: 
- Extract data of +400K invoices from Redshift 
- Transform the data by:
  - Remove Nulls
  - Remove corrupt stock codes
  - Fix column types
  - Remove duplicates

- Load the transformed data to an S3 bucket 



## Requirements
The minimum requirements:
- Docker for Mac: [Docker >= 20.10.2](https://docs.docker.com/docker-for-mac/install/)
- Docker for Windows: 
    - Installation: [Docker](https://docs.docker.com/desktop/install/windows-install/)
    - Manual installation steps for older WSL version: [Docker WSL 2](https://learn.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package)


## Instructions on how to execute the code
- Copy the `env.example` file to `.env` and fill out the environment vars.
- Make sure you are executing the code from the folder where you have your Dockerfile and python scripts and you have Docker Desktop running 

To run it locally first build the image. 

```bash
   docker image build -t etl . 
```
Then run the etl job using docker: 

```bash
docker run --env-file .env etl

```
