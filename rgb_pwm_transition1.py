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
        # delay = duration / steps
        # delay = 0.000001
        r_start, g_start, b_start = start_color
        r_end, g_end, b_end = end_color
        for i in range(steps + 1):
            r = int(min(max(r_start + (r_end - r_start) * i / steps, 0), 100))
            g = int(min(max(g_start + (g_end - g_start) * i / steps, 0), 100))
            b = int(min(max(b_start + (b_end - b_start) * i / steps, 0), 100))
            self.setColor(r, g, b)
            # time.sleep(delay)

# Define GPIO pin numbers
r_pin = 12
g_pin = 13
b_pin = 19

# Initialize RGB LED
led = RGBA(r_pin, g_pin, b_pin)

try:
    # Iterate through all RGB color combinations
    for r in range(0, 256):
        for g in range(0, 256):
            for b in range(0, 256):
                led.smoothTransition((100, 100, 100), (r, g, b), 0.000001)  # Transition to new color
                print(f"R={r}, G={g}, B={b}")
                # time.sleep(0.1)  # Pause briefly before transitioning to the next color

except KeyboardInterrupt:
    GPIO.cleanup()
    print('Quitting...')

finally:
    GPIO.cleanup()
