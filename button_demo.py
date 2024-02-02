import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

channel = 16
GPIO.setup(channel, GPIO.IN)

