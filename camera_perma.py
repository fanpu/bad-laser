from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.rotation = 270
camera.start_preview()
sleep(100000)
