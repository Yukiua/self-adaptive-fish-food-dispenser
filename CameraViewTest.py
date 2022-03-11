#This is to test whether the camera is working
import cv2
import numpy as np

video = cv2.VideoCapture("rtsp://admin:admin123456@172.20.129.250:554/av0_0")
#value of rtsp of camera. Use Device Manager to find out ip of camera and change it so that it fits in the default gateway,
# not the windows one, then use ivms to find out the rtsp after connecting the ip camera to the ivms

while True:
    _,framse = video.read()
    resized = cv2.resize(framse,(500,500),fx=0,fy=0, interpolation=cv2.INTER_LINEAR)
    #cropped = framse[0:200,200:500] - cropping the frame
    #pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]]) - if slanted
    #pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]]) - if slanted
    # matrix = cv2.getPerspectiveTransform(pts1,pts2) - transform frame
    # imgout = cv2.warpPerspective(img,matrix,(width,height))
    cv2.imshow("RTSP",np.hstack((resized,resized)))
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
