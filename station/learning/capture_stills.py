from picamera import PiCamera
from time import sleep
import datetime
import sys

camera = PiCamera()

camera.rotation = 180
camera.resolution = (360,360)

startTime = datetime.datetime.now()
timeDiff = 0

#for i in range(5):
while (timeDiff < 600):
    #camera.annotate_text = 'Test Image %s' % i
    sleep(60)
    currentDateTime = datetime.datetime.now()
    currentDateTimeString = currentDateTime.strftime("%Y%m%d%H%M%S")
    camera.capture('./pics/test_image_%s.jpg' % currentDateTimeString)
    timeDiff = (currentDateTime - startTime).total_seconds()
    print(timeDiff)

endTime = datetime.datetime.now()

totalTime = endTime - startTime

print(totalTime)
