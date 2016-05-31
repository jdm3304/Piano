import RPi.GPIO as GPIO
import time
from datetime import datetime

trigger = 17
echo = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigger, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

distanceConfig = 100

while True:
    distance = 0
    GPIO.output(trigger, True)
    time.sleep(0.00001)
    GPIO.output(trigger, False)

    while GPIO.input(echo) == 0:
        signaloff = time.time()
    while GPIO.input(echo) == 1:
        signalon = time.time()
    distance = (signalon - signloff) * 17000

    print distance
    
