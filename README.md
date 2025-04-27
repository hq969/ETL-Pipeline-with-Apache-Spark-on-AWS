# ETL-Pipeline-with-Apache-Spark-on-AWS

etl_pipeline_spark_aws/
│
├── README.md                          # Project overview, setup, and usage instructions
├── requirements.txt                   # Python dependencies
├── .env                               # Environment variables (AWS keys, DB creds)
│
├── config/
│   └── config.yaml                    # Configuration file for paths, schema, etc.
│
├── data/
│   ├── raw/                           # Raw incoming files (CSV, JSON, Parquet, etc.)
│   ├── processed/                     # Cleaned and transformed files
│   └── logs/                          # Log files and pipeline status
│
├── src/
│   ├── extract/
│   │   └── extract_data.py            # Extracts data from S3, API, or DB
│   │
│   ├── transform/
│   │   └── transform_data.py          # Data cleaning, deduplication, formatting
│   │
│   ├── load/
│   │   └── load_data.py               # Writes processed data to S3, Redshift, or RDS
│   │
│   └── utils/
│       ├── spark_session.py           # Initializes SparkSession with AWS configs
│       └── logger.py                  # Custom logger setup
│
├── jobs/
│   └── run_etl_pipeline.py           # Main script to run the complete ETL pipeline
│
├── scripts/
│   └── upload_to_s3.sh                # Bash script to upload raw files to S3
│
└── notebooks/
    └── exploratory_analysis.ipynb     # EDA or transformation check notebook
