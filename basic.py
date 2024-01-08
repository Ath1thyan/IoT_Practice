#To import the RPi.GPIO module:
import RPi.GPIO as GPIO    


# To specify which you are using using (mandatory):
GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)


# To detect which pin numbering system has been set
mode = GPIO.getmode()
print(mode)


# To disable warnings
# GPIO.setwarnings(False)


#To configure a channel as an input
channel = 19
# GPIO.setup(channel, GPIO.IN)
GPIO.setup(channel, GPIO.OUT, initial=GPIO.HIGH)


chan_list = [11,12]    # add as many channels as you want!
                       # you can tuples instead i.e.:
                       #   chan_list = (11,12)
GPIO.setup(chan_list, GPIO.OUT)


# To read the value of a GPIO pin
GPIO.input(channel)


# To set the output state of a GPIO pin:
# State can be 0 / GPIO.LOW / False or 1 / GPIO.HIGH / True.
GPIO.output(channel, state)


# output to many channels in the same call
chan_list = [11,12]                             # also works with tuples
GPIO.output(chan_list, GPIO.LOW)                # sets all to GPIO.LOW
GPIO.output(chan_list, (GPIO.HIGH, GPIO.LOW))   # sets first HIGH and second LOW


# To clean up at the end of your script:
GPIO.cleanup()


# can clean up individual channels, a list or a tuple of channels:
GPIO.cleanup(channel)
GPIO.cleanup( (channel1, channel2) )
GPIO.cleanup( [channel1, channel2] )


# To discover information about your RPi:
GPIO.RPI_INFO


# To discover the Raspberry Pi board revision:
GPIO.RPI_INFO['P1_REVISION']


# To discover the version of RPi.GPIO:
GPIO.VERSION