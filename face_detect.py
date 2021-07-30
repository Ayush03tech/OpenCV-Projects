import cv2 as cv
import numpy as np

img = cv.imread('me.jpg')
res_img = cv.resize(img, (500, 500))

cv.imshow('Face_img', res_img)

gray = cv.cvtColor(res_img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray_face', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

face_react = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

print(f'Number of faces found = {len(face_react)}')

for (x,y,w,h) in face_react:
    cv.rectangle(res_img, (x,y), (x+w, y+h), (0,255,0), thickness=3)

cv.imshow('Face_img', res_img)

cv.waitKey(0)
cv.destroyAllWindows()