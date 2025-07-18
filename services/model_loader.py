# model_loader.py

from strands.models import BedrockModel
import os

def get_bedrock_model():
    aws_region = os.getenv('AWS_REGION', 'us-east-1')
    
    return BedrockModel(
        model_id="us.amazon.nova-micro-v1:0",
        temperature=0.7,
        region_name=aws_region
    )
