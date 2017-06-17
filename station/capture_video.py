from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.rotation = 180
camera.resolution = (360,360)

camera.start_recording('./pics/test_video_10s.h264')
sleep(10)
camera.stop_recording()

# command to convert video to MP4
# MP4Box -add pics/test_video_10s.h264 pics/video.mp4
