import cv2 as cv
import  numpy as np

img = cv.imread('Valorant.png')
cv.imshow('Image', img)

# Converting into Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray_img', gray)

# blur
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Canny Edges
canny = cv.Canny(img, 125, 175
)
cv.imshow('Cannyedges', canny)

# Dilate image
dil = cv.dilate(canny, (5,5), iterations=1)
cv.imshow('dilate', dil)

# Erosion
eroded  = cv.erode(dil, (5,5), iterations=1)
cv.imshow('erosion', eroded)

# resize
resized = cv.resize(img, (960, 540), interpolation=cv.INTER_AREA)
cv.imshow('resized image', resized)

# crop 
Cropped_img = img[:]
cv.imshow('Cropped', Cropped_img)

cv.waitKey(0)
cv.destroyAllWindows()