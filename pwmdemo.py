import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

channel = 19
GPIO.setup(channel, GPIO.OUT)

frequency = 0.5
pwm_instance = GPIO.PWM(channel, frequency)

pwm_instance.start(50)

input('Enter a key to quit')
pwm_instance.stop()
GPIO.cleanup()