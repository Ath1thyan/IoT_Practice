import RPi.GPIO as GPIO
import time
from colour import Color
from threading import Thread

GPIO.setmode(GPIO.BCM)
inputChannel = 27

GPIO.setup(inputChannel, GPIO.IN)
speed = 0.1
stop = False

class RGBdemo():

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
        #print(r, g, b)
        self.r.ChangeDutyCycle(int(r))
        self.g.ChangeDutyCycle(int(g))
        self.b.ChangeDutyCycle(int(b))


# 0-100 (for colours module)
    def setRGB(self, rgb):
        r = abs(rgb[0] * 100 - 100)
        g = abs(rgb[1] * 100 - 100)
        b = abs(rgb[2] * 100 - 100)

        #print(r, g, b)

        self.r.ChangeDutyCycle(int(r))
        self.g.ChangeDutyCycle(int(g))
        self.b.ChangeDutyCycle(int(b))
        


def rgb_transition_thread(self, rgb, duration):
    
    obj = RGBdemo(12, 13, 19)
    while True:
        if stop:
            break
        for i in Color("violet").range_to(Color("indigo"), 1000):
            obj.setRGB(i.rgb)
            time.sleep(speed/100)
        for i in Color("indigo").range_to(Color("blue"), 1000):
            obj.setRGB(i.rgb)
            time.sleep(speed/100)
        for i in Color("blue").range_to(Color("green"), 1000):
            obj.setRGB(i.rgb)
            time.sleep(speed/100)
        for i in Color("green").range_to(Color("yellow"), 1000):
            obj.setRGB(i.rgb)
            time.sleep(speed/100)
        for i in Color("yellow").range_to(Color("orange"), 1000):
            obj.setRGB(i.rgb)
            time.sleep(speed/100)
        for i in Color("orange").range_to(Color("red"), 1000):
            obj.setRGB(i.rgb)
            time.sleep(speed/100)
        for i in Color("red").range_to(Color("white"), 1000):
            obj.setRGB(i.rgb)
            time.sleep(speed/100)
        for i in Color("white").range_to(Color("violet"), 1000):
            obj.setRGB(i.rgb)
            time.sleep(speed/100)


t = Thread(target = rgb_transition_thread)
t.start()
stime = time.time()

try:
    while True:
        if (GPIO.wait_for_edge(inputChannel, GPIO.RISING, timeout=1000)):
        # if (GPIO.wait_for_edge(inputChannel, GPIO.RISING, timeout=5000)):
            print("Button key down " + str(time.time()))
            stime = time.time()
        
        if (GPIO.wait_for_edge(inputChannel, GPIO.FALLING, timeout=1000)):
        # if (GPIO.wait_for_edge(inputChannel, GPIO.FALLING, timeout=5000)):
            print("Button key up " + str(time.time()))
            ltime = time.time() - stime
            #speed = ltime / 100
            speed = ltime / 10
            print("Speed: " + str(speed))
            
            
except KeyboardInterrupt:
    stop = True
    t.join()
    GPIO.cleanup()
    print("\nQuitting...")
