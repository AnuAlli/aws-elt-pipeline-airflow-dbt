from aws_cdk import Stack, aws_s3 as s3, aws_glue as glue
from constructs import Construct

class TransformStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)
        
        glue.CfnJob(
            self, "ETLJob",
            role="arn:aws:iam::ACCOUNT_ID:role/GlueServiceRole",
            command=glue.CfnJob.JobCommandProperty(
                name="glueetl",
                script_location="s3://bucket/scripts/etl.py"
            )
        )
