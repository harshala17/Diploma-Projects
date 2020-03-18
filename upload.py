import os
import boto3
from botocore.client import Config

ACCESS_KEY_ID = 'AKIAJIIFZKBPSGR2FH7Q'
ACCESS_SECRET_KEY = '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'
BUCKET_NAME = 'image-captured'

s3 = boto3.resource(
  's3',
  aws_access_key_id = ACCESS_KEY_ID,
  aws_secret_access_key = ACCESS_SECRET_KEY,
  config = Config(signature_version = 's3v4')
)

print('I am in upload python file')
os.system('fswebcam rat.jpg')
file_name = 'rat.jpg'
data = open('rat.jpg', 'rb')
s3.Bucket(BUCKET_NAME).put_object(Key = 'rat.jpg', Body = data)

# elif(up_type == 'L'
#     or up_type == 'l'):
#   print('[OPTIONAL] NAME THE IMAGE FILE AS PER THE USERNAME')
# path = raw_input("Image Path:")
# data = open('rat.jpg', 'rb')
# s3.Bucket(BUCKET_NAME).put_object(Key = '02Ian.jpg', Body = data)

#else :
  #print("Something went Wrong!!")

# data = open('target1.jpg', 'rb')# s3.Bucket(BUCKET_NAME).put_object(Key = 'target1.jpg', Body = data)

print("Done")