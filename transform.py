import cv2 as cv 
import numpy as np

img = cv.imread('Valorant.png')
cv.imshow('img', img)

# translation

def translate(img, x, y):
    transMat  = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    
    return cv.warpAffine(img, transMat, dimensions)

# x -> right
# y -> down
# -x -> left
# -y -> up

translated = translate(img, 100, 100)
cv.imshow('shifted_img', translated)

# Rotate image

def Rotate(img, angle, Rotpnt=None):
    (height, width) = (img.shape[:2])

    if Rotpnt==None:
        Rotpnt  = (width//2, height//2)

    rotmat = cv.getRotationMatrix2D(Rotpnt, angle, 1.0)
    dimensions = (height, width)

    return cv.warpAffine(img, rotmat, dimensions)

rotated = Rotate(img, 90)
cv.imshow('Rotated image', rotated)

# Fliping image
filped = cv.flip(img, 0)
cv.imshow('flipped', filped)

# Cropping 
crop = img[200:300, 300:400]
cv.imshow('Cropped', crop)

cv.waitKey(0)
cv.destroyAllWindows()
