# LD_PRELOAD=/usr/lib/arm-linux-gnueabihf/libatomic.so.1.2.0 python3 color.py

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import numpy as np
import cv2
import math

def ResizeWithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)



camera = PiCamera()
rawCapture = PiRGBArray(camera)

time.sleep(0.1)

camera.capture(rawCapture, format="bgr")
image = rawCapture.array
output = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.5, 120)

if circles is not None:
    circles = np.round(circles[0, :]).astype("int")

#     firstCircle = circles[0]
#     cv2.circle(output, (firstCircle[0],firstCircle[1]), firstCircle[2], (0,255,0),2)
#     cv2.circle(output, (firstCircle[0],firstCircle[1]), 2, (0,255,0),2)

    bigX = 0
    bigY = 0
    bigR = 0
    
    for (x,y,r) in circles:
        if r > bigR:
            bigX = x
            bigY = y
            bigR = r
            
    cv2.circle(output, (bigX,bigY), bigR, (0,255,0), 4)
    cv2.rectangle(output, (x-5, y-5), (x+5, y+5), (0, 128, 255), -1)
    
    for i in range(12):
        angle = 30 * (i)
        print(angle)
        x = bigR * math.cos(angle*0.0174532925)
        y = bigR * math.sin(angle*0.0174532925)
        cv2.line(output, (bigX, bigY), (int(x+bigX), int(y+bigY)), (0, 255, 0), 2)


#     convertedImage = np.hstack([image, output])
    cv2.imshow("output", ResizeWithAspectRatio(output, width=800))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
