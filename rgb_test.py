import RPi.GPIO as GPIO
import time

class rgb_demo():

    def __init__(self, r, g, b):

        GPIO.setmode(GPIO.BCM)

        channels_list = [r, g, b]
        for i in channels_list:
            GPIO.setup(i, GPIO.OUT)

        self.red = GPIO.PWM(r, 60)
        self.green = GPIO.PWM(g, 60)
        self.blue = GPIO.PWM(b, 60)

        self.red.start(0)
        self.green.start(0)
        self.blue.start(0)


    def setColor(self, rc, gc, bc):
        rc = 100 - (rc / 255) * 100
        gc = 100 - (gc / 255) * 100
        bc = 100 - (bc / 255) * 100

        self.red.ChangeDutyCycle(rc)
        self.green.ChangeDutyCycle(gc)
        self.blue.ChangeDutyCycle(bc)


obj = rgb_demo(12, 13, 19)
obj.setColor(255, 0, 0)
time.sleep(3)
GPIO.cleanup()