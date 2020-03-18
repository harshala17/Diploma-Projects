import os
import boto3
from botocore.client import Config

ACCESS_KEY_ID = 'AKIAID22OPKLZDX7OEAQ'
ACCESS_SECRET_KEY = '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'
BUCKET_NAME = 'image-captured'

data = open('c.jpg', 'rb')


s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version='s3v4')
)
s3.Bucket(BUCKET_NAME).put_object(Key='c.jpg', Body=data)

print ("Done")

os.system('python list-bucket.py')

