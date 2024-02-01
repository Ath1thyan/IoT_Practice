import RPi.GPIO as GPIO

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
        

    def setColor(self):
        for i in range(0, 255, 1):
            r = 100 - (i / 255) * 100
            self.r.ChangeDutyCycle(r)

        for j in range(0, 255, 1):
            g = 100 - (j / 255) * 100
            self.g.ChangeDutyCycle(g)

        for k in range(0, 255, 1):
            b = 100 - (k / 255) * 100
            self.b.ChangeDutyCycle(b)

led = RGBA(12, 13, 19)
led.setColor()
GPIO.cleanup()
