import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN) #PIR
GPIO.setup(24, GPIO.OUT) #BUzzer

try:
    time.sleep(2) # to stabilize sensor
    while True:
        if GPIO.input(23):
            os.system('python upload.py')
            os.system('python rep.py')
            print('call successfully returns to the calling python file') 
            #GPIO.output(24, True)
            #time.sleep(0.5) #Buzzer turns on for 0.5 sec
            #GPIO.output(24, False)
            print("Motion Was Detected...")
            
            time.sleep(5) #to avoid multiple detection
        time.sleep(1) #loop delay, should be less than detection delay

except:
    GPIO.cleanup() 