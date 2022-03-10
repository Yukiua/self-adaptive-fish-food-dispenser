import cv2

video = cv2.VideoCapture("rtsp://admin:admin123456@172.20.129.250:554/av0_0")
while True:
    _,framse = video.read()
    resized = cv2.resize(framse,(1080,720),fx=0,fy=0, interpolation=cv2.INTER_LINEAR)
    #cv2.imshow("Horizontal",np.hstack((img,img))) to join 2 horizontal img tgt
    #cropped = framse[0:200,200:500]
    #pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]]) - if slanted
    #pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
    # matrix = cv2.getPerspectiveTransform(pts1,pts2)
    # imgout = cv2.warpPerspective(img,matrix,(width,height))
    cv2.imshow("RTSP",resized)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
