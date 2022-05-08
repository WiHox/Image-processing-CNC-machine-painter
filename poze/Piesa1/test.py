from cmath import pi
import cv2 as cv
from cv2 import imshow
from cv2 import ROTATE_90_CLOCKWISE
import cv2
from imutils import contours
import numpy as np 
import imutils
import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk

#Get the biggest contour of the image and also in the center and ALSO a rectangular shape
def getBiggestContour(image):
    # load our input image, convert it to grayscale, and blur it slightly
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    
    cv.imshow("Image", gray)
    cv.waitKey(0)
    gray = cv.GaussianBlur(gray, (7, 7), 0)
    cv.imshow("Image", gray)
    cv.waitKey(0)
    # perform edge detection, then perform a dilation + erosion to
    # close gaps in between object edges
    edged = cv.Canny(gray, 50, 100)
    cv.imshow("Image", edged)
    cv.waitKey(0)
    edged = cv.dilate(edged, None, iterations=1)
    cv.imshow("Image", edged)
    cv.waitKey(0)
    edged = cv.erode(edged, None, iterations=1)
    cv.imshow("Image", edged)
    cv.waitKey(0)

    # find contours in the edge map
    cnts = cv.findContours(edged.copy(), cv.RETR_EXTERNAL,
	cv.CHAIN_APPROX_NONE)
    cnts = imutils.grab_contours(cnts)
    (cnts, _) = contours.sort_contours(cnts)
    box = cv.minAreaRect(cnts[0])
    box = cv.cv.BoxPoints(box) if imutils.is_cv2() else cv.boxPoints(box)
    box = np.array(box, dtype="int")
    return box


def getBiggestContour1(image):
    original_image= image

    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    
    cv.imshow("Image", gray)
    cv.waitKey(0)
    #gray = cv.GaussianBlur(gray, (7, 7), 0)
    trash, gray = cv.threshold(gray, 160 ,255, cv.THRESH_BINARY)
    cv.imshow("Image", gray)
    cv.waitKey(0)
    # perform edge detection, then perform a dilation + erosion to
    # close gaps in between object edges
    edged = cv.Canny(gray, 90, 230) 
    cv.imshow("Image", edged) 
    cv.waitKey(0)
    
    edged = cv.dilate(edged, None, iterations=1)
    cv.imshow("Image", edged)
    cv.waitKey(0)
    
    edged = cv.erode(edged, None, iterations=1)
    cv.imshow("Image", edged)
    cv.waitKey(0)
    
    contours, hierarchy= cv.findContours(edged.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    
    sorted_contours= sorted(contours, key=cv.contourArea, reverse= True)

    largest_item = sorted_contours[0]

    cv.drawContours(original_image, [largest_item], -1, (0, 0, 225), 5)

    cv.imshow('Largest Object', original_image)
    cv.waitKey(0)

    epsilon = 0.04 * cv.arcLength(largest_item, True)
    largest_item = cv.approxPolyDP(largest_item, epsilon, True)
    #sort_largest_items(largest_item)
    print(largest_item)

    return largest_item


nameOfFile = "C:\\Users\\Razvan Wiho\\EdgeDetectionCNCMachinePainting\\poze\\Piesa1\\pozaTest1.jpg"
im2 = cv.imread(nameOfFile)
a = getBiggestContour1(im2)
print("------------------")
print(a)


