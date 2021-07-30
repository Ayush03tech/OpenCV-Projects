import cv2 as cv
import numpy as np

image = cv.imread('Valorant.png')
# cv.imshow('image', image)

resized_img = cv.resize(image, (960, 540))
cv.imshow('Image', resized_img)

# Average
blur = cv.blur(resized_img, (5,5))
cv.imshow('Average_blur', blur)

# Gaussian Blur
guass = cv.GaussianBlur(resized_img, (5,5), 0)
cv.imshow('Gauss_blur', guass)

# median blur
med = cv.medianBlur(resized_img, 5)
cv.imshow('MEdian_blur', med)

# Bilateral blur
bi = cv.bilateralFilter(resized_img, 3, 10, 15)
cv.imshow('Bilateral blur', bi)

cv.waitKey(0)
cv.destroyAllWindows()
