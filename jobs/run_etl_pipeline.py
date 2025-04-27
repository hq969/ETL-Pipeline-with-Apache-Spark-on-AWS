import os
from dotenv import load_dotenv
from src.utils.spark_session import create_spark_session
from src.extract.extract_data import extract_from_s3
from src.transform.transform_data import transform_data
from src.load.load_data import load_to_s3
import yaml

load_dotenv()

with open("config/config.yaml", 'r') as file:
    config = yaml.safe_load(file)

spark = create_spark_session()
logger = spark._jvm.org.apache.log4j.LogManager.getLogger("ETLJob")

raw_file = "data/raw/input.csv"
extract_from_s3(config['s3']['bucket_name'], config['s3']['raw_path'] + "input.csv", raw_file)
df_clean = transform_data(spark, raw_file)
load_to_s3(df_clean, config['s3']['processed_path'])
