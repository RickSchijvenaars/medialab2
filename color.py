# LD_PRELOAD=/usr/lib/arm-linux-gnueabihf/libatomic.so.1.2.0 python3 color.py

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import numpy as np
import cv2


camera = PiCamera()
rawCapture = PiRGBArray(camera)

time.sleep(0.1)

camera.capture(rawCapture, format="bgr")
image = rawCapture.array
output = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)

if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    
    for (x,y,r) in circles:
        cv2.circle(output, (x,y), r, (0,255,0), 4)
        cv2.rectangle(output, (x-5, y-5), (x+5, y+5), (0, 128, 255), -1)

    convertedImage = np.hstack([image, output])
    cv2.imshow("output", cv2.resize(convertedImage, (800,400)))
    cv2.waitKey(0)


