# Daniel Ryaboshapka
# feb 24 2020
# testcamera.py 

import cv2 
import serial 
from picamera.array import PiRGBArray
from picamera import PiCamera
import time 
import numpy as np

camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 15
rawCapture = PiRGBArray(camera, size=(320, 240))

time.sleep(.5)
red_boundary = ([0,0,100], [90,40,255])
lower , upper = red_boundary
lower = np.array(lower, dtype="uint8")
upper = np.array(upper, dtype="uint8")

font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
font_color = (255, 255, 255)
org = (70,230)
thickness = 1

s=serial.Serial("/dev/serial0",9600,timeout=10)
s.write("hello".encode())
time.sleep(1)
s.read(s.inWaiting())
print("Sent hello")

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    
    image = frame.array
    temp = cv2.resize(image, (32,24), interpolation=cv2.INTER_LINEAR)
    output = cv2.resize(temp, (320,240), interpolation=cv2.INTER_NEAREST)
    #cv2.imshow("Frame", output)

    mask = cv2.inRange(output, lower, upper)
    output2 = cv2.bitwise_and(output,output, mask=mask)
    average = np.average(output2)
    threshold = 5.8
    if s.inWaiting() != 0:
        wait = s.read()
        time.sleep(.4)
        if average > threshold:
            print("sent red")
            s.write("1".encode())
        else:
            print("sent no red")
            s.write("0".encode())
    if average > threshold:
        output = cv2.putText(output, 'RED DETECTED', org, font, fontScale, font_color,
                            thickness, cv2.LINE_AA)
    #cv2.imshow("frame", output)
    key = cv2.waitKey(1)

    rawCapture.truncate(0)

    if key == ord("q"):
        camera.close()
        break


