## 🚀 ETL Pipeline with Apache Spark on AWS

A modular, production-grade ETL pipeline built using Apache Spark and AWS services (S3, Redshift, RDS).
The pipeline extracts raw data from Amazon S3, transforms it using PySpark, and loads the cleaned data back into S3 or a database.

etl_pipeline_spark_aws/

├── config/             # Configuration files

├── data/               # Raw and processed data

├── jobs/               # ETL pipeline runner

├── notebooks/          # Exploratory data analysis

├── scripts/            # Shell scripts for automation

├── src/                # Source code for ETL stages and utilities

├── .env                # Environment variables (AWS keys, DB creds)

├── README.md           # Project overview

└── requirements.txt    # Python dependencies

------------------------------------------------------------------------------------------------------------------------------------

## ⚙️ Technologies Used

- Apache Spark (PySpark)
- AWS S3 (Storage)
- AWS Redshift/RDS (Optional — Data warehouse)
- Python 3.13
- Boto3 (AWS SDK for Python)
- YAML (Configuration Management)

-----------------------------------------------------------------------------------------------------------------------------------

## 🏗️ How the ETL Pipeline Works

1. Extract
- Pull raw CSV/JSON/Parquet files from an S3 bucket.
  
2. Transform
- Data cleaning: removing nulls, duplicates, schema enforcement.
- Additional transformations as required.

3. Load
- Save transformed data back into S3 as Parquet files or load into Redshift/RDS.

------------------------------------------------------------------------------------------------------------------------------------

## 🔥 Quick Start

1. Clone the repository

git clone https://github.com/hq969/ETL-Pipeline-with-Apache-Spark-on-AWS.git
cd ETL-Pipeline-with-Apache-Spark-on-AWS

2. Set up environment
   
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

3. Configure AWS credentials

Create a .env file:

AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_REGION=your_region

Edit the config/config.yaml file to match your S3 paths and database settings.

4. Run the ETL job

python jobs/run_etl_pipeline.py


---------------------------------------------------------------------------------------------------------------------------------

## 🛡️ Best Practices Followed

- Modular and scalable ETL structure
- Environment-based configuration
- Logging and error handling
- Clean separation of concerns (extract/transform/load)

## 📊 Future Improvements

- Orchestration with Airflow or AWS Step Functions
- Add unit and integration tests
- Dockerize the project for portability
- Monitor using AWS CloudWatch

## 👨‍💻 Author

Harsh Sonkar





