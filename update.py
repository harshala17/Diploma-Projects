import os
import boto3
import RPi.GPIO as GPIO
import time
from botocore.client import Config


ACCESS_KEY_ID = 'AKIAJDSSLNDFPAOEFPPQ'
ACCESS_SECRET_KEY = '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'
BUCKET_NAME = 'image-captured'
            
s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version='s3v4')
   )
GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN) #PIR

try:
    time.sleep(2) # to stabilize sensor
    while True:
        if GPIO.input(23):
            os.system('fswebcam rat.jpg')
            data = open('rat.jpg', 'rb')
            s3.Bucket(BUCKET_NAME).put_object(Key='rat.jpg', Body=data)
            GPIO.cleanup()
            os.system('python rep.py')
            print('Done')
            #sys.path.insert("Desktop/rekon")
            os.system("rm rat.jpg")
           # time.sleep(5) #to avoid multiple detection
        time.sleep(1) #loop delay, should be less than detection delay
            
except:
    os.system('python update.py')