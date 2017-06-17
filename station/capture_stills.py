from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.rotation = 180
camera.resolution = (360,360)

for i in range(5):
    camera.annotate_text = 'Test Image %s' % i
    sleep(5)
    camera.capture('./pics/test_image_%s.jpg' % i)
