#!/usr/bin/env python3
import aws_cdk as cdk
from stacks.ingest_stack import IngestStack
from stacks.transform_stack import TransformStack

app = cdk.App()
IngestStack(app, "IngestStack")
TransformStack(app, "TransformStack")
app.synth()
