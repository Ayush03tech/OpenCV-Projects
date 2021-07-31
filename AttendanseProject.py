import cv2 as cv 
import face_recognition as face
import numpy as np

import os

path = 'Pics'
images = []
classname = []
mylist = os.listdir(path)

for cl in mylist:
    currimg = cv.imread(f'{path}\{cl}')
    images.append(currimg)
    classname.append(os.path.splitext(cl)[0])

print(classname)
print(images)
print(mylist)