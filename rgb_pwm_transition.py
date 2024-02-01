import RPi.GPIO as GPIO
import time

class RGBA():
    def __init__(self, r, g, b):
        GPIO.setmode(GPIO.BCM)
        self.r_pin = r
        self.g_pin = g
        self.b_pin = b
        self.frequency = 1000  # Set PWM frequency to 1000 Hz
        GPIO.setup(self.r_pin, GPIO.OUT)
        GPIO.setup(self.g_pin, GPIO.OUT)
        GPIO.setup(self.b_pin, GPIO.OUT)
        self.r_pwm = GPIO.PWM(self.r_pin, self.frequency)
        self.g_pwm = GPIO.PWM(self.g_pin, self.frequency)
        self.b_pwm = GPIO.PWM(self.b_pin, self.frequency)
        self.r_pwm.start(0)
        self.g_pwm.start(0)
        self.b_pwm.start(0)

    def setColor(self, r, g, b):
        self.r_pwm.ChangeDutyCycle(r)
        self.g_pwm.ChangeDutyCycle(g)
        self.b_pwm.ChangeDutyCycle(b)

    def smoothTransition(self, start_color, end_color, duration):
        steps = 100  # Number of steps for transition
        delay = duration / steps
        r_start, g_start, b_start = start_color
        r_end, g_end, b_end = end_color
        for i in range(steps + 1):
            r = min(max(r_start + (r_end - r_start) * i / steps, 0), 100)
            g = min(max(g_start + (g_end - g_start) * i / steps, 0), 100)
            b = min(max(b_start + (b_end - b_start) * i / steps, 0), 100)
            print(f"Step {i}: R={r}, G={g}, B={b}")
            self.setColor(r, g, b)
            time.sleep(delay)

# Define GPIO pin numbers
r_pin = 12
g_pin = 13
b_pin = 19

# Initialize RGB LED
led = RGBA(r_pin, g_pin, b_pin)

try:
    # Smoothly transition between colors
    led.smoothTransition((255, 0, 0), (0, 255, 0), 5)  # Red to Green transition over 5 seconds
    led.smoothTransition((0, 255, 0), (0, 0, 255), 5)  # Green to Blue transition over 5 seconds
    led.smoothTransition((0, 0, 255), (255, 0, 0), 5)  # Blue to Red transition over 5 seconds

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
