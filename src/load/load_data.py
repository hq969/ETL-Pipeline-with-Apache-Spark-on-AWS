def load_to_s3(df, output_path):
    df.write.mode("overwrite").parquet(output_path)
