import RPi.GPIO as GPIO
import time

class RGBA():
    def __init__(self, r, g, b):
        channel_list = [r, g, b]
        GPIO.setmode(GPIO.BCM)
        for c in channel_list:
	        GPIO.setup(channel_list, GPIO.OUT)
		self.r = GPIO.PWM(r, 60)
		self.g = GPIO.PWM(g, 60)
		self.b = GPIO.PWM(b, 60)
        

    def setColor(self, r, g, b):
    	r =((r / 255) * 100)
		g =((g / 255) * 100)
		b =((b / 255) * 100)

		self.r.ChangeDutyCycly(r)
		self.g.ChangeDutyCycly(g)
		self.b.ChangeDutyCycly(b)

		led = RGBA(12, 13, 19)
		led.setColor(255,0,0)
		time.sleep(3)