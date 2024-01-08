import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
channel =[12, 13, 19]

for c in channel:
	GPIO.setup(c, GPIO.OUT)

try:
	while True:
		try:
			i= input("Enter a num between 0-7: ")
			i=int(i)

			if(i<0 or i>=8):
				print("Invalid input, Try again...")
				continue
			rgb = format(i, '03b')
			for i, c in enumerate(channel): 
				GPIO.output(c, not bool(int(rgb[i])))

		except ValueError:
			print("Invalid input, Try again...")

except KeyboardInterrupt:
	GPIO.cleanup()
	print("Quitting...")