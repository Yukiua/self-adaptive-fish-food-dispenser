#This file is to find detect the contour of the object by applying colour masking with HSV to of the relevant BGR of the object

import cv2,numpy as np

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture("rtsp://admin:admin123456@172.20.129.250:554/av0_0")
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,150)
myColor = [[52,46,27,141,170,255],[133,56,0,159,156,255],[57,76,0,100,255,255]] #HSV value for masking
myColorValues = [[51,153,255],[255,0,255],[0,255,0]] #BGR of object to detect

def findColor(img,myColor):
    #Finds all instances of the colour range within the frame
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    for color in myColor:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV,lower,upper)
        getContours(mask)

def getContours(img):
    #Finds the contour outline of the detected colour range
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area>500:
            cv2.drawContours(imgResult,cnt,-1,(255,0,0),3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x,y,w,h = cv2.boundingRect(approx)

while True:
    success, img = cap.read()
    imgResult = img.copy()
    findColor(img, myColor)
    cv2.imshow("Object Detection", cv2.resize(imgResult,(720,500),fx=0,fy=0, interpolation=cv2.INTER_LINEAR))
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
