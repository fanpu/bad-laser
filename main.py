import time
import wiringpi

# Row 2: output from pin 18, input for top servo
# Row 10: output from pin 13, input for bottom servo

wiringpi.wiringPiSetupGpio()

PIN1 = 13 #bottom
PIN2 = 18 #top

# Sets PWM output 
wiringpi.pinMode(PIN1, wiringpi.GPIO.PWM_OUTPUT)
wiringpi.pinMode(PIN2, wiringpi.GPIO.PWM_OUTPUT)


wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

delay_period = 0.003

# wiringpi.pwmWrite(PIN1, 150)

while True:
        for pulse in range(0, 300, 1):
                wiringpi.pwmWrite(PIN1, pulse)
                wiringpi.pwmWrite(PIN2, pulse)
                time.sleep(delay_period)
        for pulse in range(250, 50, -1):
                wiringpi.pwmWrite(PIN1, pulse)
                wiringpi.pwmWrite(PIN2, pulse)
                time.sleep(delay_period)
