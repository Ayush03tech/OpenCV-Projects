import cv2 as cv
import numpy as np

# Function for resize

def Rescaling(frame, scale = 0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# resizeing image
 
img = cv.imread('Valorant.png')
cv.imshow('Image', img)

resized_image = Rescaling(img)
cv.imshow('resized_img', resized_image)

# resizing Video

video = cv.VideoCapture('video.mp4')

while True:
    isTrue , frame = video.read()
    # frame_resized = Rescaling(frame)

    cv.imshow('Video', frame)
    # cv.imshow('video_resized', frame_resized)

    if cv.waitKey(0) & 0xFF == ord('d'):
        break
video.release()

cv.waitKey(0)
cv.destroyAllWindows()

