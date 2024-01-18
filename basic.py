
                ##############################      BASICS      ###################################

#To import the RPi.GPIO module:
import RPi.GPIO as GPIO 

import time   


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


                ###################################     INPUT       #########################################

# If you do not have the input pin connected to anything, it will 'float'. In other words, the value that is read in is undefined because it is not connected to anything until you press a button or switch. It will probably change value a lot as a result of receiving mains interference.
# To get round this, we use a pull up or a pull down resistor. In this way, the default value of the input can be set. It is possible to have pull up/down resistors in hardware and using software. In hardware, a 10K resistor between the input channel and 3.3V (pull-up) or 0V (pull-down) is commonly used. The RPi.GPIO module allows you to configure the Broadcom SOC to do this in software:
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#   # or
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


# To take a snapshot of an input at a moment in time:
if GPIO.input(channel):
    print('Input was HIGH')
else:
    print('Input was LOW')


# To wait for a button press by polling in a loop:
while GPIO.input(channel) == GPIO.LOW:
    time.sleep(0.01)  # wait 10 ms to give CPU chance to do other things


# wait_for_edge() function
# The wait_for_edge() function is designed to block execution of your program until an edge is detected. In other words, the example above that waits for a button press could be rewritten as:
GPIO.wait_for_edge(channel, GPIO.RISING)
# Note that you can detect edges of type GPIO.RISING, GPIO.FALLING or GPIO.BOTH. The advantage of doing it this way is that it uses a negligible amount of CPU, so there is plenty left for other tasks.


# If you only want to wait for a certain length of time, you can use the timeout parameter:
# # wait for up to 5 seconds for a rising edge (timeout is in milliseconds)
channel = GPIO.wait_for_edge(channel, GPIO_RISING, timeout=5000)
if channel is None:
    print('Timeout occurred')
else:
    print('Edge detected on channel', channel)


# The event_detected() function is designed to be used in a loop with other things, but unlike polling it is not going to miss the change in state of an input while the CPU is busy working on other things. This could be useful when using something like Pygame or PyQt where there is a main loop listening and responding to GUI events in a timely basis.
GPIO.add_event_detect(channel, GPIO.RISING)  # add rising edge detection on a channel
do_something()
if GPIO.event_detected(channel):
    print('Button pressed')
# Note that you can detect events for GPIO.RISING, GPIO.FALLING or GPIO.BOTH.
    

# RPi.GPIO runs a second thread for callback functions. This means that callback functions can be run at the same time as your main program, in immediate response to an edge. For example:
def my_callback(channel):
    print('This is a edge event callback function!')
    print('Edge detected on channel %s'%channel)
    print('This is run in a different thread to your main program')
GPIO.add_event_detect(channel, GPIO.RISING, callback=my_callback)  # add rising edge detection on a channel
# ...the rest of your program...


# If you wanted more than one callback function:
def my_callback_one(channel):
    print('Callback one')
def my_callback_two(channel):
    print('Callback two')
GPIO.add_event_detect(channel, GPIO.RISING)
GPIO.add_event_callback(channel, my_callback_one)
GPIO.add_event_callback(channel, my_callback_two)
# Note that in this case, the callback functions are run sequentially, not concurrently. This is because there is only one thread used for callbacks, in which every callback is run, in the order in which they have been defined.


#### Switch debounce  ####
# You may notice that the callbacks are called more than once for each button press. This is as a result of what is known as 'switch bounce'. There are two ways of dealing with switch bounce:
    # add a 0.1uF capacitor across your switch.
    # software debouncing
    # a combination of both
# To debounce using software, add the bouncetime= parameter to a function where you specify a callback function. Bouncetime should be specified in milliseconds. For example:
# add rising edge detection on a channel, ignoring further edges for 200ms for switch bounce handling
GPIO.add_event_detect(channel, GPIO.RISING, callback=my_callback, bouncetime=200)
    # or
GPIO.add_event_callback(channel, my_callback, bouncetime=200)


# Remove event detection
# If for some reason, your program no longer wishes to detect edge events, it is possible to stop them:
GPIO.remove_event_detect(channel)


                ######################################      OUTPUT      ##########################################

# To set up RPi.GPIO (as described here)
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)


# To set an output high:
GPIO.output(12, GPIO.HIGH)
 # or
GPIO.output(12, 1)
 # or
GPIO.output(12, True)


# To set an output low:
GPIO.output(12, GPIO.LOW)
 # or
GPIO.output(12, 0)
 # or
GPIO.output(12, False)


# To output to several channels at the same time:
chan_list = (11,12)
GPIO.output(chan_list, GPIO.LOW) # all LOW
GPIO.output(chan_list, (GPIO.HIGH,GPIO.LOW))  # first LOW, second HIGH


# To read the current state of a channel set up as an output using the input() function. For example to toggle an output:
GPIO.output(12, not GPIO.input(12))


# Clean up at the end of your program
GPIO.cleanup()


                ##############################       gpio_function(channel)      ################################

# Shows the function of a GPIO channel.
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
func = GPIO.gpio_function(pin)
# will return a value from:
# GPIO.IN, GPIO.OUT, GPIO.SPI, GPIO.I2C, GPIO.HARD_PWM, GPIO.SERIAL, GPIO.UNKNOWN


                #################################       P W M     #######################################

# To create a PWM instance:
p = GPIO.PWM(channel, frequency)


# To start PWM:
p.start(dc)   # where dc is the duty cycle (0.0 <= dc <= 100.0)


# To change the frequency:
p.ChangeFrequency(freq)   # where freq is the new frequency in Hz


# To change the duty cycle:
p.ChangeDutyCycle(dc)  # where 0.0 <= dc <= 100.0


# To stop PWM:
p.stop()

# Note that PWM will also stop if the instance variable 'p' goes out of scope.


# An example to blink an LED once every two seconds:
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
p = GPIO.PWM(12, 0.5)
p.start(1)
input('Press return to stop:')   # use raw_input for Python 2
p.stop()
GPIO.cleanup()


# An example to brighten/dim an LED:
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
p = GPIO.PWM(12, 50)  # channel=12 frequency=50Hz
p.start(0)
try:
    while 1:
        for dc in range(0, 101, 5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100, -1, -5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()