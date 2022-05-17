import cv2
import numpy as np

"""
Assorted functions for conversion, contour finding, etc
"""

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

def calc_whitepixels(filled_contour):
    height, width = filled_contour.shape[0], filled_contour.shape[1]
    img_mean = cv2.mean(filled_contour)[0]/255

    pixels = height * width
    #print("Total image pixels:", pixels)

    area = img_mean * pixels
    #print("white pixel filled:", area)

    percentage = area / pixels * 100
    print("percentage filled:", percentage)
    return percentage


def img_threshold(img):
    blurred = cv2.GaussianBlur(img, (5, 5), 0)
    thresh = cv2.threshold(blurred, 12, 255, cv2.THRESH_BINARY)[1]
    return thresh