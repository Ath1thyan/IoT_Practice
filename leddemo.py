import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(True)

channel = 16
GPIO.setup(channel, GPIO.OUT)

try:
	while True:
		GPIO.output(channel, GPIO.HIGH)

except KeyboardInterrupt:
	GPIO.cleanup()
	print("Quitting...")