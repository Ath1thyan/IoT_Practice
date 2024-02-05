import RPi.GPIO as GPIO
import time
from colour import Color
import math

class rgb_demo():

    def __init__(self, r, g, b):

        GPIO.setmode(GPIO.BCM)

        channels_list = [r, g, b]
        for i in channels_list:
            GPIO.setup(i, GPIO.OUT)

        self.r = GPIO.PWM(r, 60)
        self.g = GPIO.PWM(g, 60)
        self.b = GPIO.PWM(b, 60)

        self.r.start(0)
        self.g.start(0)
        self.b.start(0)


# for 0-255 rgb values
    def setColor(self, r, g, b):
        r = 100 - (r / 255) * 100
        g = 100 - (g / 255) * 100
        b = 100 - (b / 255) * 100
        print(r, g, b)
        self.r.ChangeDutyCycle(int(r))
        self.g.ChangeDutyCycle(int(g))
        self.b.ChangeDutyCycle(int(b))


# 0-100 (for colours module)
    def setRGB(self, rgb):
        r = abs(rgb[0] * 100 - 100)
        g = abs(rgb[1] * 100 - 100)
        b = abs(rgb[2] * 100 - 100)

        print(r, g, b)

        self.r.ChangeDutyCycle(int(r))
        self.g.ChangeDutyCycle(int(g))
        self.b.ChangeDutyCycle(int(b))

obj = rgb_demo(12, 13, 19)
# obj.setColor(255, 0, 0)
try:
    # get a color as input

    # while True:
    #     obj.setRGB(Color(input("Enter any color: ")).rgb)
    #     time.sleep(3)


    # color to color in loop
    # c = Color("red").range_to(Color("blue"), 100)
    # for i in c:
    #     obj.setRGB(i.rgb)
    #     time.sleep(0.1)


    # looping from color to color again & again
    # rtb = Color("red").range_to(Color("blue"), 100)
    # btr = Color("blue").range_to(Color("red"), 100)
    # while True:
    #     for i in rtb:
    #         obj.setRGB(i.rgb)
    #         time.sleep(0.01)
    #     for i in btr:
    #         obj.setRGB(i.rgb)
    #         time.sleep(0.01)


    # looping from color to color again & again in infinite loop
    while True:
        for i in Color("red").range_to(Color("blue"), 100):
            obj.setRGB(i.rgb)
            time.sleep(0.01)
        for i in Color("blue").range_to(Color("red"), 100):
            obj.setRGB(i.rgb)
            time.sleep(0.01)

    GPIO.cleanup()
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nQuitting...")