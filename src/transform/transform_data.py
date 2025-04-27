from pyspark.sql import SparkSession

def transform_data(spark, input_path):
    df = spark.read.csv(input_path, header=True, inferSchema=True)
    df_clean = df.dropna().dropDuplicates()
    return df_clean
