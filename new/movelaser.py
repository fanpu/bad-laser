import numpy as np
import cv2
import sys
import threading
from picamera import PiCamera
import time
import wiringpi
from setup import PIN1, PIN2, DELAY, setup
from motion.motion import Direction
# PIN1: bottom
# 50: left
# 250: right

# PIN2: top


# topleft: (176, 143)
# bottomright: (125, 167)


io = setup()

FRAME_WIDTH = 224 #416 #1920
FRAME_HEIGHT = 160 #304 #1088
MOTOR_TOP = 143
MOTOR_BOTTOM = 167
MOTOR_LEFT = 176
MOTOR_RIGHT = 125
                

wiringpi.pwmWrite(PIN1, 150)
time.sleep(1)
wiringpi.pwmWrite(PIN2, 150)
time.sleep(1)
prevy = 150
prevx = 150
motorx = 150
motory = 150

def readpos():
    global motorx
    global motory
    while True:
        pos = input()
        motorx, motory = pos.split(" ")
        motorx = int(motorx)
        motory = int(motory)

t = threading.Thread(target=readpos)
t.daemon = True
t.start()

while True:
    if motorx != prevx or motory != prevy:
        if motorx != prevx:
            cdir = 1 if (motorx > prevx) else -1
            dist = abs(motorx - prevx)
            prevx = motorx if (dist < 3) else (prevx + cdir * 3)
            wiringpi.pwmWrite(PIN1, prevx)
            time.sleep(DELAY)
        if motory != prevy:
            cdir = 1 if (motory > prevy) else -1
            dist = abs(motory - prevy)
            prevy = motory if (dist < 3) else (prevy + cdir * 3)
            wiringpi.pwmWrite(PIN2, prevy)
            time.sleep(DELAY)
    # camera.annotate_text = '%d; %f %f; %d %d' % (len(faces), posx, posy, motorx, motory)
