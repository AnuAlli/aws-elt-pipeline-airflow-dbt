from aws_cdk import Stack, aws_s3 as s3, aws_lambda as _lambda
from constructs import Construct

class IngestStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)
        
        bucket = s3.Bucket(self, "RawDataBucket")
        
        lambda_fn = _lambda.Function(
            self, "IngestFunction",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="handler.handler",
            code=_lambda.Code.from_asset("lambda")
        )
        
        bucket.grant_read_write(lambda_fn)
