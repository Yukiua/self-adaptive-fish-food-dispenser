import jetson.inference
import jetson.utils
import cv2
import numpy as np

net = jetson.inference.detectNet("ssd-mobilenet-v2",threshold=0.5)
cap = cv2.VideoCapture("rtsp://admin:admin123456@172.20.129.23:10700/cam/realmonitor?channel=1&subtype=0")
cap.set(3,640)
cap.set(4,480)

while True:
    success,img = cap.read()
    imgcuda = jetson.utils.cudaFromNumpy(img)
    detect = net.Detect(imgcuda)
    for d in detect:
        x1,y1,x2,y2 = int(d.Left),int(d.Top),int(d.Right),int(d.Bottom)
        classname = net.GetClassDesc(d.ClassID)
        cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,255),2)
        cv2.putText(img,classname,(x1+5,y1+15),cv2.FONT_HERSHEY_COMPLEX,0.75,(255,0,255),2)
    resize = cv2.resize(img,(500,500),fx=0,fy=0,interpolation=cv2.INTER_LINEAR)
    cv2.imshow("172.20.129.23:10700",resize)
    k = cv2.waitKey(1)
    if k==ord('q'):break
cap.release()
cv2.destroyAllWindows()