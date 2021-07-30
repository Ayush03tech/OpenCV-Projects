import cv2 as cv
import numpy as np

img = cv.imread('Valorant.png')

cv.imshow('image', img)

# painting the whole image or specific area

img[200:300, 400:800] = (0,0,255)
cv.imshow('Red', img)

# Drawing reactangle
cv.rectangle(img, (0,0), (500,500), (0,0,255),  thickness=3)
cv.imshow('draw_img', img)

# Drawing circle
cv.circle(img, (960,540), 40, (0,0,255), thickness=3)
cv.imshow('Circle_img', img)

# Drawing a line
cv.line(img, (0,0), (960, 540), (255,255,255), thickness=3)
cv.imshow('line', img)

# Write Text
cv.putText(img, 'Ayush', (960, 540), cv.FONT_HERSHEY_PLAIN, 5, (255,0,0), thickness=2)
cv.imshow('text', img)

cv.waitKey(0)
cv.destroyAllWindows()
