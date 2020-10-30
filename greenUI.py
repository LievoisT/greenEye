import cv2
# from picamera import PiCamera
# from sense_hat import SenseHat
# from picamera.array import PiRGBArray
import serial
import time
import numpy as np

while True:

    img = np.zeros((480, 640, 3), np.uint8)

    img = cv2.line(img, (500, 470), (400, 350), (255, 255, 255), 1, lineType=cv2.LINE_AA)
    img = cv2.line(img, (500, 470), (600, 350), (255, 255, 255), 1, lineType=cv2.LINE_AA)

    
    x_locals = np.arange(400, 620, 20)
    for i in range(10):
        methane = np.random.rand()
        pts = np.array([[500, 470], [x_locals[i], 350], [x_locals[i+1], 350]], np.int32)
        pts = pts.reshape((-1, 1, 2))
        img = cv2.fillPoly(img, [pts], (int(255 * methane), 0, 0))

    time.sleep(0.2)
    # pts = np.array([[500, 470], [400, 350], [420, 350]], np.int32)
    # pts = pts.reshape((-1, 1, 2))
    # img = cv2.polylines(img, [pts], True, (255, 255, 255))

    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
