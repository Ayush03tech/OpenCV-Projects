import cv2 as cv
from face_recognition.api import face_locations
import numpy as np
import face_recognition as face

import os

from numpy.lib.type_check import imag

path = 'Pics'
images = []
classname = []
mylist = os.listdir(path)

for cl in mylist:
    curimg = cv.imread(f"{path}/{cl}")
    images.append(curimg)
    classname.append(os.path.splitext(cl)[0])

def findEncoding(images):
    EncodeList = []
    for img in images:
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        encode = face.face_encodings(img)[0]
        EncodeList.append(encode)

    return EncodeList
encodingList_known = findEncoding(images)
print('Encoding Complete.')

cap = cv.VideoCapture(0)

while True:
    success, img = cap.read()
    imgs = cv.resize(img, (0,0), None, 0.25,0.25)

    facesCurFrame = face.face_locations(imgs)
    EncodesCurFrame = face.face_encodings(imgs, facesCurFrame)
    
    for encodeFace, faceloc in zip(EncodesCurFrame, facesCurFrame):
        matches = face.compare_faces(encodingList_known, encodeFace)
        facedis = face.face_distance(encodingList_known, encodeFace)
        matchindex = np.argmin(facedis)

        if matches[matchindex]:
            name = classname[matchindex].upper()
            print(name)
            y1, x2, y2, x1 = faceloc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv.rectangle(img, (x1, y1), (x2,y2), (0,255,0), 2)
            cv.rectangle(img, (x1,y2-35), (x2,y2), (0,255,0), cv.FILLED)
            cv.putText(img, name, (x1+6, y2-6), cv.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)

    cv.imshow('webcam', img)

    cv.waitKey(1)