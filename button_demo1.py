import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
channel = 27

GPIO.setup(channel, GPIO.IN)
while True:
    if (GPIO.wait_for_edge(channel, GPIO.RISING, timeout=1000)):
        print("Button key down " + str(time.time()))
        
    if (GPIO.wait_for_edge(channel, GPIO.FALLING, timeout=1000)):
        print("Button key up " + str(time.time()))