import time
import RPi.GPIO as GPIO
 
#mqttc = mqtt.Client("pi")
#mqttc.connect("127.0.0.1", 8080)
 
trig_pin = 13
echo_pin = 19
 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setup(trig_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)
 
global ultrasonic
 
try:
    while True:
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
 
        ultrasonic = distance
 
        print "Distance : ", ultrasonic, "cm"
 
except KeyboardInterrupt:
    GPIO.cleanup()
 
