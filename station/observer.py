from picamera import PiCamera
from envirophat import weather
from time import sleep
import datetime
import sys

camera = PiCamera()

camera.rotation = 180
camera.resolution = (360,360)

startTime = datetime.datetime.now()
timeDiff = 0
out = open('station.log', 'w')
out.write('temp,pressure,image,time\n')

#for i in range(5):
while (timeDiff < 300):
    #camera.annotate_text = 'Test Image %s' % i
    sleep(60)
    currentDateTime = datetime.datetime.now()
    currentDateTimeString = currentDateTime.strftime("%Y%m%d%H%M%S")
    currentTempCelsius = weather.temperature()
    currentPressure = weather.pressure()
    imageName = ('./pics/test_image_%s.jpg' % currentDateTimeString)
    camera.capture(imageName)
    out.write('%s\t%s\t%s\t%s\n' % (currentTempCelsius, currentPressure, imageName, currentDateTime)) 
    timeDiff = (currentDateTime - startTime).total_seconds()
    print(timeDiff)

out.close()
endTime = datetime.datetime.now()

totalTime = endTime - startTime

print(totalTime)
