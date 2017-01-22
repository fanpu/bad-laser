import time
import wiringpi

# Row 2: output from pin 18, input for top servo
# Row 10: output from pin 13, input for bottom servo

PIN1 = 13 #bottom
PIN2 = 18 #top
# DELAY = 0.01
DELAY = 0.05
CENTER_TOP = 150
CENTER_BOTTOM = 150
ROTATE_LEFT = 1
ROTATE_RIGHT = 1
ROTATE_UP = 1
ROTATE_DOWN = 1


def setup():

    io = "kek"
    # io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_PINS)

    # io.pinMode(PIN1, io.PWM_OUTPUT)
    
    wiringpi.wiringPiSetupGpio()

    # Sets PWM output 
    wiringpi.pinMode(PIN1, wiringpi.GPIO.PWM_OUTPUT)
    wiringpi.pinMode(PIN2, wiringpi.GPIO.PWM_OUTPUT)


    wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

    wiringpi.pwmSetClock(192)
    wiringpi.pwmSetRange(2000)

    return io

