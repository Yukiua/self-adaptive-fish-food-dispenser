##WARNING: File does not work if there is no single large contour found!!!
# Place a large, well-lit area in front of the camera as the while loop will fail

import cv2
import numpy as np
from StackingVideos import stackImages

frameWidth = 640
frameHeight = 480
widthImg = 720
heightImg = 500
cap = cv2.VideoCapture("rtsp://admin:admin123456@172.20.129.23:10700/cam/realmonitor?channel=1&subtype=0")
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)


def preProcess(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
    imgCanny = cv2.Canny(imgBlur, 200, 200)
    kernel = np.ones((5, 5))
    imgDial = cv2.dilate(imgCanny, kernel, iterations=2)
    imgThresh = cv2.erode(imgDial, kernel, iterations=1)
    return imgThresh


def getContours(img):
    biggest = np.array([])
    max = 0
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 5000:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            if area > max and len(approx) == 4:
                biggest = approx
                max = area
    cv2.drawContours(imgContour, biggest, -1, (255, 0, 0), 3)
    return biggest


def sortOrder(point):
    point = point.reshape((4, 2))
    newpoint = np.zeros((4, 1, 2), np.int32)
    add = point.sum(1)
    newpoint[0] = point[np.argmin(add)]
    newpoint[3] = point[np.argmax(add)]
    diff = np.diff(point, axis=1)
    newpoint[1] = point[np.argmin(diff)]
    newpoint[2] = point[np.argmax(diff)]
    return newpoint


def getWarp(img, biggest):
    biggest = sortOrder(biggest)
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgout = cv2.warpPerspective(img, matrix, (widthImg, heightImg))
    return imgout


def allcontour():
    imgContour = img.copy()
    imgThresh = preProcess(img)
    getContours(imgThresh)
    return imgContour


while True:
    success, img = cap.read()
    img = cv2.resize(img, (widthImg, heightImg), fx=0, fy=0, interpolation=cv2.INTER_LINEAR)
    imgContour = img.copy()
    imgThresh = preProcess(img)
    biggest = getContours(imgThresh)
    if biggest.size != 0:
        imageWarp = getWarp(img, biggest)
        imageArray = ([img, imgThresh], [imgContour, imageWarp])
    else:
        imageArray = ([img, imgThresh], [img, img])
    stacked = stackImages(0.6, imageArray)
    cv2.imshow("Object Detection", stacked)
    k = cv2.waitKey(1)
    if k == ord('q'): break