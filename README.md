# aws-elt-pipeline-airflow-dbt

![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![CDK](https://img.shields.io/badge/AWS%20CDK-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)

## Overview
A scalable data engineering pipeline built with AWS CDK.

## 🏗️ Architecture

![Architecture](assets/architecture.gif)

## Tech Stack
- **IaC:** AWS CDK (Python)
- **Compute:** AWS Lambda / Glue
- **Storage:** Amazon S3
- **Analytics:** Amazon Athena

## 📂 Project Structure
```
aws-elt-pipeline-airflow-dbt/
├── app.py
├── cdk.json
├── stacks/
│   ├── ingest_stack.py
│   ├── transform_stack.py
│   └── analytics_stack.py
├── lambda/
│   └── etl_handler.py
└── requirements.txt
```

## 🚀 Getting Started
```bash
pip install -r requirements.txt
cdk bootstrap
cdk deploy --all
```

## License
MIT
