import cv2 as cv
import numpy as np

img = cv.imread('Valorant.png')
re_img = cv.resize(img, (960, 540))

blank = np.zeros(re_img.shape[:2], dtype='uint8')

cv.imshow('Image', re_img)

mask = cv.circle(blank, (re_img.shape[1]//2, re_img.shape[0]//2) ,100,  255, -1)

masked = cv.bitwise_and(re_img, re_img, mask=mask)
cv.imshow('Masked_img', masked)


cv.waitKey(0)
cv.destroyAllWindows()