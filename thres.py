import cv2 as cv
import numpy as np

img = cv.imread('valorant.png')
res = cv.resize(img, (960, 540))
# Gray
gray = cv.cvtColor(res, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple Threshold
threshold, thres = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
# cv.imshow('Threshold_image', threshold)
cv.imshow('Thres_image', thres)

# Adaptive Threshold
adap = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 5)
cv.imshow('Adaptive threshold', adap)


cv.waitKey(0)
cv.destroyAllWindows()