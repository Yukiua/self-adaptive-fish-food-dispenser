#This Python file is to determine the value of mask needed for the tracker to filter out stuff

import cv2, numpy as np
cap = cv2.VideoCapture("rtsp://admin:admin123456@172.20.129.250:554/av0_0")
myColor = []


def empty(a):
    pass

cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 640, 240)
#Change accordingly to mask out objects irrelvant to detect
cv2.createTrackbar("HUE MIN", "HSV", 0, 179, empty)
cv2.createTrackbar("SAT MIN", "HSV", 0, 255, empty)
cv2.createTrackbar("VALUE MIN", "HSV", 0, 255, empty)
cv2.createTrackbar("HUE MAX", "HSV", 179, 179, empty)
cv2.createTrackbar("SAT MAX", "HSV", 255, 255, empty)
cv2.createTrackbar("VALUE MAX", "HSV", 255, 255, empty)

while True:
    _, img = cap.read()
    img = cv2.resize(img,(500,500),fx=0,fy=0, interpolation=cv2.INTER_LINEAR)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("HUE MIN", "HSV")
    h_max = cv2.getTrackbarPos("HUE MAX", "HSV")
    s_min = cv2.getTrackbarPos("SAT MIN", "HSV")
    s_max = cv2.getTrackbarPos("SAT MAX", "HSV")
    v_min = cv2.getTrackbarPos("VALUE MIN", "HSV")
    v_max = cv2.getTrackbarPos("VALUE MAX", "HSV")
    print(h_min)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max,v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    cv2.imshow("Hori", np.hstack((img,mask,result)))
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()