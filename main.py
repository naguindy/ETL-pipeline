import os

# library to read passwords
from dotenv import load_dotenv

# import connect_to_redshift from extract script
from src.extract import extract_transaction_data
from src.transform import drop_duplicates
from src.load_data_to_s3 import df_to_s3


load_dotenv()

dbname = os.getenv('dbname')
host = os.getenv('host')
port = os.getenv('port')
user = os.getenv('user')
password = os.getenv('password')
aws_access_key_id = os.getenv("aws_access_key_id")
aws_secret_access_key_id = os.getenv("aws_secret_access_key_id")
#extract data with transformation
online_trans_cleaned = extract_transaction_data(dbname, host, port, user, password)
print('The shape of the extracted and transformed is:', online_trans_cleaned.shape)
#drop duplicates
online_trans_cleaned_no_dup = drop_duplicates(online_trans_cleaned)

#loading the date to s3
s3_bucket = 'july-bootcamp'
key = 'etl_pipeline/ng_online_transactions_v2.pkl'
df_to_s3(online_trans_cleaned_no_dup, key, s3_bucket, aws_access_key_id, aws_secret_access_key_id)
