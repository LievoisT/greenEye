import os
import serial
import cv2
import numpy as np
import time
from picamera.array import PiRGBArray
from picamera import PiCamera
from sense_hat import SenseHat

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
sense = SenseHat()

rawCapture = PiRGBArray(camera)
time.sleep(0.1)

x_locals = np.arange(400, 620, 20)
# polys = []
colors = []
for i in range(10):
#     pts = np.array([[500, 470], [x_locals[i], 350], [x_locals[i+1], 350]], np.int32)
#     pts = pts.reshape((-1, 1, 2))
#     polys.append(pts)
    colors.append(255)


for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    o = sense.get_orientation()
    yaw = o["yaw"]
    methane = np.random.rand()

    #grabs a numpy array and a time stamp

    image = frame.array
    image = cv2.line(image, (500, 470), (400, 350), (255, 255, 255), 1, lineType=cv2.LINE_AA)
    image = cv2.line(image, (500, 470), (600, 350), (255, 255, 255), 1, lineType=cv2.LINE_AA)
    print(int(yaw))

    if int(yaw) >= 90 & int(yaw) <= 180:
        index = int((yaw-90)/9)
        print("in zone: " + str(index))
        colors[index] = int(methane * 255)

    for i in range(10):
        pts = np.array([[500, 470], [x_locals[i], 350], [x_locals[i+1], 350]], np.int32)
        pts = pts.reshape((-1, 1, 2))
        image = cv2.fillPoly(image, [pts], (255, 255, 255-colors[i]))
    

    cv2.imshow("Frame", image)

    key = cv2.waitKey(1) & 0xFF

    rawCapture.truncate(0)

    if key == ord("q"):
        break