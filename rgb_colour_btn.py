import RPi.GPIO as GPIO
import time
from colour import Color
from threading import Thread

GPIO.setmode(GPIO.BCM)
inputChannel = 27

GPIO.setup(inputChannel, GPIO.IN)
speed = 0.1

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
        
    

# class RGBTransitionThread(Thread):
#     def __init__(self, rgb, start, end, duration):
#         Thread.__init__(self)
#         self.rgb = rgb
#         self.duration = duration
#         self.start_t = start
#         self.end_t = end
#         self.stoprequest = False


def rgb_transition_thread(self, rgb, duration):
    # start = time.time()
    # while time.time() - start <  duration:
        # self.setRGB(rgb)
        # time.sleep(0.01)
        
        while True:
            for i in Color("red").range_to(Color("blue"), 100):
                obj.setRGB(i.rgb)
                time.sleep(speed)
            for i in Color("blue").range_to(Color("red"), 100):
                obj.setRGB(i.rgb)
                time.sleep(speed)


t = Thread(target = rgb_transition_thread)
t.start()

try:
    while True:
        if GPIO.input(inputChannel) == GPIO.HIGH:
            # print("Button Pressed " + str(time.time()))
            if stime is None:
                stime = time.time()
            else:
                speed = time.time() - stime
                print("Speed: " + str(speed))
                stime = None
                
            time.sleep(0.01)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nQuitting...")


obj = rgb_demo(12, 13, 19)
GPIO.cleanup()