import os
import time
import RPi.GPIO as GPIO

trig_pin = 13
echo_pin = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(trig_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)

try:
    while True:
        GPIO.output(trig_pin, False)
        time.sleep(0.5)
        GPIO.output(trig_pin, True)
        time.sleep(0.00001)
        GPIO.output(trig_pin, False)

        while GPIO.input(echo_pin) == 0:
            pulse_start = time.time()

        while GPIO.input(echo_pin) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17000
        distance = round(distance, 2)

        print "Distance : ", distance, "cm"

        if 3 <= distance <= 5:
            os.system("aplay DO1.WAV")
 
        if 7 <= distance <= 9:
            os.system("aplay RE.WAV")

        if 11 <= distance <= 13:
            os.system("aplay MI.WAV")

        if 15 <= distance <= 17:
            os.system("aplay FA.WAV")

        if 19 <= distance <= 21:
            os.system("aplay SOL.WAV")

        if 23 <= distance <= 25:
            os.system("aplay RA.WAV")

        if 27 <= distance <= 29:
            os.system("aplay SI.WAV")

        if 31 <= distance <= 33:
            os.system("aplay DO@.WAV")

except:
    GPIO.cleanup()
