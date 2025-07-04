# from ctypes.wintypes import RGB
import RPi.GPIO as GPIO
import time

class RGBA():
    def __init__(self, r, g, b):
        GPIO.setmode(GPIO.BCM)
        channel_list = [r, g, b]
        for c in channel_list:
            GPIO.setup(c, GPIO.OUT)
        self.r = GPIO.PWM(r, 60)
        self.g = GPIO.PWM(g, 60)
        self.b = GPIO.PWM(b, 60)
        self.r.start(0)
        self.g.start(0)
        self.b.start(0)
        

    def setColor(self, r, g, b):
        r = 100 - (r / 255) * 100
        g = 100 - (g / 255) * 100
        b = 100 - (b / 255) * 100

        self.r.ChangeDutyCycle(r)
        self.g.ChangeDutyCycle(g)
        self.b.ChangeDutyCycle(b)

led = RGBA(12, 13, 19)
led.setColor(0,0,255)
time.sleep(3)
GPIO.cleanup()
