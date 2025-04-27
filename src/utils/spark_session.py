from pyspark.sql import SparkSession

def create_spark_session(app_name="ETLApp"):
    spark = SparkSession.builder \
        .appName(app_name) \
        .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:3.2.0") \
        .getOrCreate()
    return spark
