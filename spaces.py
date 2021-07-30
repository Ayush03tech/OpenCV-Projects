import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt

img = cv.imread('Valorant.png')
# cv.imshow('image', img)

resize = cv.resize(img, (960, 540))

# plt.imshow(resize)
# plt.show()

# BGR to Gray
gray = cv.cvtColor(resize, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

BGR  = cv.cvtColor(gray, cv.COLOR_GRAY2RGB)
cv.imshow('gray --> bgr', BGR)

# HSV
HSV = cv.cvtColor(resize, cv.COLOR_BGR2HSV)
cv.imshow('HSV', HSV)

# LAB
lab = cv.cvtColor(resize, cv.COLOR_BGR2LAB)
cv.imshow('LAb', lab)


cv.waitKey(0)
cv.destroyAllWindows()
