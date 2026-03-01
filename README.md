# **aws elt pipeline airflow dbt**

![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![CDK](https://img.shields.io/badge/AWS%20CDK-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)

## Overview
Production-ready data engineering pipeline built with AWS CDK, featuring comprehensive infrastructure as code, monitoring, and error handling.

## 🏗️ Architecture

![Architecture](assets/architecture.gif)

## Features

- **Infrastructure as Code**: Full AWS CDK implementation with Type-Safe constructs
- **Production Ready**: Error handling, logging, metrics, and retries
- **Monitoring**: CloudWatch metrics, dashboards, and alerting
- **Secure**: Least-privilege IAM roles, encrypted storage
- **Scalable**: Auto-scaling capabilities and efficient resource usage

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| IaC | AWS CDK (Python) |
| Compute | AWS Lambda / Glue |
| Storage | Amazon S3 |
| Analytics | Amazon Athena |
| Monitoring | CloudWatch |

## 📂 Project Structure

```
$(basename $project)/
├── app.py                    # CDK App entry point
├── cdk.json                  # CDK configuration
├── requirements.txt          # Python dependencies
├── stacks/
│   ├── __init__.py
│   ├── ingest_stack.py       # Data ingestion infrastructure
│   ├── transform_stack.py    # Data transformation infrastructure
│   └── analytics_stack.py    # Analytics infrastructure
├── lambda/
│   └── etl_handler.py        # Lambda function code
├── glue/
│   └── etl_job.py            # Glue job scripts
└── assets/
    └── architecture.gif      # Architecture diagram
```

## 🚀 Getting Started

### Prerequisites

- AWS CLI configured with appropriate credentials
- Python 3.11+
- Node.js 18+
- AWS CDK (`npm install -g aws-cdk`)

### Installation

```bash
# Clone the repository
git clone https://github.com/AnuAlli/$(basename $project).git
cd $(basename $project)

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Bootstrap CDK (first time only)
cdk bootstrap

# Deploy stacks
cdk deploy --all
```

### Configuration

Set required environment variables:

```bash
export DATA_BUCKET_NAME=your-bucket-name
export ENVIRONMENT=production
```

## 📊 Monitoring

This project includes CloudWatch metrics for:

- Records processed
- Processing latency
- Error rates
- Data volume

## 🧪 Testing

```bash
# Run unit tests
pytest tests/

# Run integration tests
pytest tests/ -k integration
```

## 📝 License

MIT License - feel free to use for your portfolio!
