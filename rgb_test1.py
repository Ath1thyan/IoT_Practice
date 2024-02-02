import RPi.GPIO as GPIO
import time
try:
    class rgb_demo():

        def __init__(self, r, g, b):

            GPIO.setmode(GPIO.BCM)

            channels_list = [r, g, b]
            for i in channels_list:
                GPIO.setup(i, GPIO.OUT)

            self.red = GPIO.PWM(r, 1)
            self.green = GPIO.PWM(g, 1)
            self.blue = GPIO.PWM(b, 1)

            self.red.start(0)
            self.green.start(0)
            self.blue.start(0)


        def setColor(self):
            for i in range(0, 255, 1):
                rc = 100 - (i / 255) * 100
                self.red.ChangeDutyCycle(rc)
                

                for j in range(0,255,1):
                    gc = 100 - (j / 255) * 100
                    self.green.ChangeDutyCycle(gc)
                    

                    for k in range(0, 255, 1):
                        bc = 100 - (k / 255) * 100
                        self.blue.ChangeDutyCycle(bc)
                    


    obj = rgb_demo(12, 13, 19)
    obj.setColor()
    GPIO.cleanup()

except KeyboardInterrupt:
    GPIO.cleanup()