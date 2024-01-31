import RPi.GPIO as GPIO

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
 
 
 
#  import RPi.GPIO as GPIO

# GPIO.setmode(GPIO.BCM)

# channel_list = [12,13,19]
# for c in channel_list:
# 	GPIO.setup(channel_list, GPIO.OUT)


# try:
# 	while True:
# 		try:
# 			i = input("Enter a num between 0 & 7: ")
# 			i = int(i)

# 			if i<0 or i>=8:
# 				print('invalid input, Try again...')
# 				continue

# 			rgb = format(i, '03b')
# 			for index, channel in enumerate(channel_list):
# 				GPIO.output(channel, not bool(int(rgb[index])))
# 				print(index, channel, rgb[index])
				

# 		except ValueError:
# 			print('invalid input, Try again...')
# 			continue

# except KeyboardInterrupt:
# 	GPIO.cleanup()
# 	print("\nQuitting...")