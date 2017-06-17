from picamera import PiCamera
from time import sleep

camera = PiCamera()

##camera.rotation = 180
##camera.start_preview()
##sleep(10)
##camera.stop_preview()


# rotation
# camera.rotation = 180 (flip image upside down)


# still pictures
# should sleep for at least 2 seconds so light levels can be set
# camera.capture('name_of_image.jpg')
# the line above goes between the start/stop preview lines


# camera.start_preview()
# for i in range(5):
#     sleep(5)
#     camera.capture('/home/darren/Desktop/image%s.jpg' % i)
# camera.stop_preview()
camera.rotation = 180
camera.resolution = (360,360)
#camera.start_preview()
camera.annotate_text = "Test Image 3"
sleep(5)
camera.capture('./pics/test_image.jpg')
#camera.stop_preview


# VIDEO
# camera.start_preview()
# camera.start_recording('name_of_video_file')
# sleep(10)
    # camera.stop_recording()
# camera.stop_preview()


# PROPERTIES
# camera.resolution = (x, y)
# camera.framerate = z
# camera.annotate_text = "text here"
# camera.annotation_text_size = 6 to 160 (default 32)
# camera.brightness = p
# camera.contrast = q
