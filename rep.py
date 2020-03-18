import boto3
import RPi.GPIO as GPIO
import time
import boto3

from botocore.client import Config

Buzzer = 26

def setup(pin):
    global BuzzerPin
    BuzzerPin = pin
    GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by physical location
    GPIO.setup(BuzzerPin, GPIO.OUT)
    GPIO.output(BuzzerPin, GPIO.HIGH)
    GPIO.setwarnings(False)

def on():
    GPIO.setwarnings(False)
    GPIO.output(BuzzerPin, GPIO.HIGH)

def off():
    GPIO.setwarnings(False)
    GPIO.output(BuzzerPin, GPIO.LOW)

BUCKET = "image-captured"
KEY = "rat.jpg"
print"i am in rep.py"
def detect_labels(bucket, key, max_labels=10, min_confidence=90, region="ap-south-1"):
    rekognition = boto3.client("rekognition",'ap-south-1')
    response = rekognition.detect_labels(
        Image={
            "S3Object": {
                "Bucket": BUCKET,
                "Name": KEY,
            }
        },
        MaxLabels=1,
        MinConfidence=50,
    )
    return response['Labels']

def ram():
        for label in detect_labels(BUCKET, KEY):
            a = "{Name} ".format(**label)            
            print"(a)- {Confidence}%"
            return a
x = str(ram())
rat='Rat'
ro='Rodent'
am='Animal'
print (x)
print "       * * * *  *        *   ********  *******   ******* "
print "     *          *        *   *         *         *       "
print "    *           *        *   *         *         *       "
print "    *    *****  *        *   ******    *******   ******* "
print "     *     * *  *        *   *               *         * "
print "      ****** *  **********   ********  *******   ******* "
print "++++++++++++++++++++++That is a {}++++++++++++++++++++++".format(x)


setup(Buzzer)
if rat in x:
    on()
elif ro in x:
    on()
elif am in x:
    on()
    
else:
    off()


