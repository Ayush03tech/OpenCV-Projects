import cv2 as cv
import numpy as np

# Reading image
img  = cv.imread('Valorant.png')

cv.imshow('image', img)

# Reading video

video = cv.VideoCapture('video.mp4')

while True:
    isTrue , frame = video.read()

    cv.imshow('Video', frame)

    if cv.waitKey(0) & 0xFF == ord('d'):
        break
video.release()

cv.waitKey(0)
cv.destroyAllWindows()
