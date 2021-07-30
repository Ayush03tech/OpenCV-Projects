import cv2 as cv
import numpy as np

img = cv.imread('Valorant.png')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Laplacion
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacion', lap)

# sobel 
sobelx = cv.Sobel(gray, cv.CV_64F, 0, 1)
sobely = cv.Sobel(gray, cv.CV_64F, 1, 0)
combine = cv.bitwise_or(sobelx, sobely)


cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Combined', combine)

cv.waitKey(0)
cv.destroyAllWindows()