import cv2 as cv
from face_recognition.api import face_distance, face_locations
import numpy as np
import face_recognition as f

imgChris = f.load_image_file('Chris evans.jfif')
imgChris = cv.cvtColor(imgChris, cv.COLOR_BGR2RGB)

imgChris2 = f.load_image_file('chris evans(2).jfif')
imgChris2 = cv.cvtColor(imgChris2, cv.COLOR_BGR2RGB)

faceloc = f.face_locations(imgChris)[1]
encodeChris = f.face_encodings(imgChris)[0]
cv.rectangle(imgChris, (faceloc[3], faceloc[0]), (faceloc[1], faceloc[2]), (255,0,255), 1)

cv.putText(imgChris, 'Chris Evans', (30,30), fontFace=cv.FONT_HERSHEY_PLAIN, fontScale=1, color=(0,0,255), thickness=1)

cv.imshow('Chris Evans', imgChris)
cv.imshow('Chris Evans(2)', imgChris2)

print(faceloc)

cv.waitKey(0)
# cv.destroyAllWindows()