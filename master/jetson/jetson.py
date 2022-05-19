#This Python file is to check if all the cameras are connected. 172.20.129.23 is the router's WAN and 10700~ etc are the ports of the cameras
#Create a static IPv4 for the cameras and port forward it to a specific port
#RTSP user is admin, password is admin123456
import cv2
import numpy as np
import time

frameWidth = 640
frameHeight = 480
widthImg = 360
heightImg = 250

video1 = cv2.VideoCapture("rtsp://admin:admin123456@172.20.129.23:10700/cam/realmonitor?channel=1&subtype=0")
video1.set(3,frameWidth)
video1.set(4,frameHeight)
video1.set(10,150)

video2 = cv2.VideoCapture("rtsp://admin:admin123456@172.20.129.23:10701/cam/realmonitor?channel=1&subtype=0")
video2.set(3,frameWidth)
video2.set(4,frameHeight)
video2.set(10,150)

video3 = cv2.VideoCapture("rtsp://admin:admin123456@172.20.129.23:10702/cam/realmonitor?channel=1&subtype=0")
video3.set(3,frameWidth)
video3.set(4,frameHeight)
video3.set(10,150)

video4 = cv2.VideoCapture("rtsp://admin:admin123456@172.20.129.23:10703/cam/realmonitor?channel=1&subtype=0")
video4.set(3,frameWidth)
video4.set(4,frameHeight)
video4.set(10,150)

video5 = cv2.VideoCapture("rtsp://admin:admin123456@172.20.129.23:10710/cam/realmonitor?channel=1&subtype=0")
video5.set(3,frameWidth)
video5.set(4,frameHeight)
video5.set(10,150)

video6 = cv2.VideoCapture("rtsp://admin:admin123456@172.20.129.23:10711/cam/realmonitor?channel=1&subtype=0")
video6.set(3,frameWidth)
video6.set(4,frameHeight)
video6.set(10,150)

while True:
    try:
        success1,img1 = video1.read()
        success2,img2 = video2.read()
        success3,img3 = video3.read()
        success4,img4 = video4.read()
        success5,img5 = video5.read()
        success6,img6 = video6.read()

        img1 = cv2.resize(img1,(widthImg,heightImg),fx=0,fy=0,interpolation=cv2.INTER_LINEAR)
        img2 = cv2.resize(img2,(widthImg,heightImg),fx=0,fy=0,interpolation=cv2.INTER_LINEAR)
        img3 = cv2.resize(img3,(widthImg,heightImg),fx=0,fy=0,interpolation=cv2.INTER_LINEAR)
        img4 = cv2.resize(img4,(widthImg,heightImg),fx=0,fy=0,interpolation=cv2.INTER_LINEAR)
        img5 = cv2.resize(img5,(widthImg,heightImg),fx=0,fy=0,interpolation=cv2.INTER_LINEAR)
        img6 = cv2.resize(img6,(widthImg,heightImg),fx=0,fy=0,interpolation=cv2.INTER_LINEAR)
        vert = np.vstack((np.hstack((img1,img2)),np.hstack((img3,img4)),np.hstack((img5,img6))))
        cv2.imshow("All", vert)
        k = cv2.waitKey(1)
        if k == ord('q'):break
    except:
        time.sleep(1)
        continue