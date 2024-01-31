import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

channel = 19
GPIO.setup(channel, GPIO.OUT)

frequency = 0.5
pwm_instance = GPIO.PWM(channel, frequency)

pwm_instance.start(100)

i = None

try:
	while i != 'q':

		try:
			d = input('set a duty cycle: ')
			f = input('set a frequency: ')

			if(d == 'q' or f == 'q'):
				GPIO.cleanup()
				break

			pwm_instance.ChangeFrequency(int(f))
			pwm_instance.ChangeDutyCycle(int(d))

		except ValueError as e:
			pass

except KeyboardInterrupt as e:
	print("Received Ctrl+C --> Quitting...")
	GPIO.cleanup()
	pass
