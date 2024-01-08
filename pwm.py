import RPi.GPIO as GPIO

chanl = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(chanl, GPIO.OUT)

p = GPIO.PWM(chanl, 0.5)
p.start(50)
i = None
try :
	while i != 'q':
		try :
			d = input('DutyCycle: ')
			f = input('Frequency: ')

			if (d=='q' or f=='q'):
				break

			p.ChangeDutyCycle(int(d))
			p.ChangeFrequency(int(f))

		except ValueError as e:
			pass

except KeyboardInterrupt as e:
	print ("Ctrl + C is received --> Quitting...")
	pass

p.stop()
GPIO.cleanup()
print ("I am Exiting...")