import RPi.GPIO as GPIO
import time
GPIO.cleanup()
chnl=[12,13,19]
freq=0.5
GPIO.setmode(GPIO.BCM)

for c in chnl:
    GPIO.setup(c, GPIO.OUT)
    p = GPIO.PWM(c, freq)
    p.start(50)
