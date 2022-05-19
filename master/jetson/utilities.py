import datetime
import cv2
import numpy as np
import firebase_admin
from firebase_admin import credentials,db

# takes contour from predicted output and draws it on original image
def draw_contour(img_pred, img_original):
    cnt = cv2.findContours(img_pred, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    img_contour = cv2.drawContours(img_original, cnt[0], -1, (64, 224, 208), 3)
    return img_contour


# takes contour from predicted output and fills it on blank image
def draw_filled_contour(img_pred, img_size):
    cnt = cv2.findContours(img_pred, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    blank_image = np.zeros((img_size[0], img_size[1], 3), np.uint8)
    filled_contour = cv2.drawContours(blank_image, cnt[0], -1, (255, 255, 255), -1)
    return filled_contour

#Calculates contours filled in proportion to the image feed
def calc_whitepixels(filled_contour):
    height, width = filled_contour.shape[0], filled_contour.shape[1]
    img_mean = cv2.mean(filled_contour)[0]/255

    pixels = height * width
    area = img_mean * pixels
    percentage = area / pixels * 100
    print("Percentage filled:", percentage)
    return percentage

def img_threshold(img):
    blurred = cv2.GaussianBlur(img, (5, 5), 0)
    thresh = cv2.threshold(blurred, 12, 255, cv2.THRESH_BINARY)[1]
    return thresh

def firebase(motorPercent):
    cred = credentials.Certificate("CERTIFICATE.json")
    firebase_admin.initialize_app(cred,{'databaseURL': 'https://DATABASE.app'})
    ref = db.reference('raspberrypi/')
    users_ref = ref.child('motor')
    fulldatetime = str(datetime.datetime.now())
    dateE = fulldatetime.split(' ')[0]
    timeE = fulldatetime.split(' ')[1].split('.')[0]
    #TODO: Depending on project scope + stepper motor specs, change this
    #Stepper Motor: More Speed = Less Feed Dropped, Less Speed, More Feed Dropped
    if(1 <= motorPercent <= 15):motor = 0.6
    elif(15 <= motorPercent <= 35):motor = 0.75
    elif(35 <= motorPercent):motor = 0.9
    elif(motorPercent == 0): motor = 0
    #The motor speed is has a range depending on its RPM, in which it is 10-15 RPM.
    #This value is sent to Firebase, and will be retrieved in the rpi
    users_ref.child("{0};{1}".format(dateE,timeE)).set({"Motor":motor})
    handle = db.reference('raspberrypi/motor/{0};{1}'.format(dateE,timeE))
