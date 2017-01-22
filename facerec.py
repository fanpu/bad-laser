import cv2
import sys
from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.rotation = 270
# camera.start_preview()
camera.capture('/tmp/frame.jpg')
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('/tmp/frame.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(gray, 1.1, 3)
print(len(faces))
if len(faces) > 0:
    (x, y, w, h) = faces[0]
    crop_img = img[y:y+h, x:x+w]
    cv2.imwrite('/tmp/crop.jpg', crop_img)

# sleep(10)
# camera.stop_preview()
