import boto3
import os
from dotenv import load_dotenv

load_dotenv()
s3 = boto3.client('s3')

def extract_from_s3(bucket, key, download_path):
    s3.download_file(bucket, key, download_path)
