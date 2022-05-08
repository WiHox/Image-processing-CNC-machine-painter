import cv2 as cv
from imutils import contours
import numpy as np 
import imutils

#Get the biggest contour of the image and also in the center and ALSO a rectangular shape
def getBiggestContour(image):
    original_image= image

    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    
    #cv.imshow("Image", gray)
    #cv.waitKey(0)
    #gray = cv.GaussianBlur(gray, (7, 7), 0)
    trash, gray = cv.threshold(gray, 160 ,255, cv.THRESH_BINARY)
    #cv.imshow("Image", gray)
    #cv.waitKey(0)
    # perform edge detection, then perform a dilation + erosion to
    # close gaps in between object edges
    edged = cv.Canny(gray, 90, 230) 
    #cv.imshow("Image", edged) 
    #cv.waitKey(0)
    
    edged = cv.dilate(edged, None, iterations=1)
    #cv.imshow("Image", edged)
    #cv.waitKey(0)
    
    edged = cv.erode(edged, None, iterations=1)
    #cv.imshow("Image", edged)
    #cv.waitKey(0)
    
    contours, hierarchy= cv.findContours(edged.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    
    sorted_contours= sorted(contours, key=cv.contourArea, reverse= True)

    largest_item = sorted_contours[0]

    cv.drawContours(original_image, [largest_item], -1, (0, 0, 225), 5)

    cv.imshow('Largest Object', original_image)
    cv.waitKey(0)

    epsilon = 0.04 * cv.arcLength(largest_item, True)
    largest_item = cv.approxPolyDP(largest_item, epsilon, True)

    return largest_item
