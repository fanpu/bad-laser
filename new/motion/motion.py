import wiringpi
from setup import DELAY, PIN1, PIN2, CENTER_BOTTOM, CENTER_TOP, ROTATE_LEFT, ROTATE_RIGHT, ROTATE_UP, ROTATE_DOWN

class Direction():
    def turnLeft():
        pass
    
    def turnRight():
        pass

    def bottomCenter():
        wiringpi.pwmWrite(PIN1, 150)
        pass

    def topCenter():
        pass
    
    def turnUp():
        pass

    def turnDown():
        pass
