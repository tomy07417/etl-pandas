import boto3
from config import REGION, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
import pandas as pd
from io import BytesIO

s3_client = boto3.client(
    's3',
    region_name=REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

def get_file_from_s3(bucket_name, file_path):
    response = s3_client.get_object(Bucket=bucket_name, Key=file_path)
    return BytesIO(response['Body'].read())

def upload_file_to_s3(bucket_name, file_path, data):
    if isinstance(data, pd.DataFrame):
        data = data.to_parquet(index=False, engine='pyarrow')

    s3_client.put_object(Bucket=bucket_name, Key=file_path, Body=data)