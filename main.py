import numpy as np
import cv2
import sys
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


# wiringpi.pwmWrite(PIN1, 250)
# io.pwmWrite(PIN1, 250)
# time.sleep(1)
# io.pwmWrite(PIN1, 50)
# wiringpi.pwmWrite(PIN1, 50)
#for pulse in range(250, 50, -1):
#    wiringpi.pwmWrite(PIN1, pulse)
#    time.sleep(DELAY)

if False:
    wiringpi.pwmWrite(PIN1, 125)
    time.sleep(DELAY)
    wiringpi.pwmWrite(PIN2, 143)

while False:
        q = input("Select a direction: " )
        if q == "left":
                turnLeft()

while False:
        for pulse in range(50, 250, 1):
                # wiringpi.pwmWrite(PIN1, pulse)
                wiringpi.pwmWrite(PIN2, pulse)
                time.sleep(DELAY)
        for pulse in range(250, 50, -1):
                wiringpi.pwmWrite(PIN1, pulse)
                time.sleep(DELAY)

FRAME_WIDTH = 224 #416 #1920
FRAME_HEIGHT = 160 #304 #1088
MOTOR_TOP = 143
MOTOR_BOTTOM = 167
MOTOR_LEFT = 176
MOTOR_RIGHT = 125
                

camera = PiCamera()
camera.start_preview()
camera.annotate_text = "PRAISE KEK!"
camera.rotation = 270
camera.resolution = (FRAME_WIDTH, FRAME_HEIGHT)
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

wiringpi.pwmWrite(PIN1, 150)
time.sleep(1)
wiringpi.pwmWrite(PIN2, 150)
time.sleep(1)
prevx = 150
prevy = 150

camera.annotate_text = ''

img = np.empty((FRAME_HEIGHT, FRAME_WIDTH, 3), dtype=np.uint8)
while True:
    camera.capture(img, 'bgr')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.1, 3)
    if len(faces) > 0:
        maxsz = 0
        bestindex = 0
        for i in range(len(faces)):
            (x, y, w, h) = faces[i]
            if w * h > maxsz:
                maxsz = w * h
                bestindex = i
        (x, y, w, h) = faces[bestindex]
        posx = x + w / 2
        posy = y + h / 2
        posy = FRAME_HEIGHT - posy - 1
        posx = FRAME_WIDTH - posx - 1
        fracx = float(posx) / float(FRAME_WIDTH)
        fracy = float(posy) / float(FRAME_HEIGHT)
        motorx = int(MOTOR_LEFT * fracx + MOTOR_RIGHT * (1 - fracx))
        motory = int(MOTOR_TOP * fracy + MOTOR_BOTTOM * (1 - fracy))
        while motorx != prevx or motory != prevy:
            if motorx != prevx:
                prevx += 1 if (motorx > prevx) else -1
                wiringpi.pwmWrite(PIN1, prevx)
                time.sleep(DELAY)
            if motory != prevy:
                prevy += 1 if (motory > prevy) else -1
                wiringpi.pwmWrite(PIN2, prevy)
                time.sleep(DELAY)
        # camera.annotate_text = '%d; %f %f; %d %d' % (len(faces), posx, posy, motorx, motory)
    else:
        # camera.annotate_text = 'no faces'
        pass
