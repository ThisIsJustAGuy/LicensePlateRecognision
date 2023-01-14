import time
import RPi.GPIO as GPIO

def green_light():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(24, GPIO.OUT)
    GPIO.output(24,True)
    time.sleep(5)
    GPIO.output(24,False)

def red_light():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(23, GPIO.OUT)
    GPIO.output(23,True)
    time.sleep(5)
    GPIO.output(23,False)
    
def red_fast():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(23, GPIO.OUT)
    for x in range(20):
        GPIO.output(23,True)
        time.sleep(0.3)
        GPIO.output(23,False)
        time.sleep(0.3)

def red_slow():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(23, GPIO.OUT)
    for x in range(6):
        GPIO.output(23,True)
        time.sleep(1)
        GPIO.output(23,False)
        time.sleep(1)
