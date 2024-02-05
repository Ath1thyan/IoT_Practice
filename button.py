import RPi.GPIO as GPIO
import time
from threading import Thread

GPIO.setmode(GPIO.BCM)
channel = 27

GPIO.setup(channel, GPIO.IN)
while True:
    if GPIO.input(channel) == GPIO.HIGH:
        print("Button Pressed " + str(time.time()))
        time.sleep(0.1)