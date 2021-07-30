import cv2 as cv
import numpy as np

img = cv.imread('Valorant.png')
resized_img = cv.resize(img, (960, 540))
cv.imshow('image', resized_img)

# spliting the RGB or BGR iamge

b,g,r = cv.split(resized_img)

cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

print(resized_img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# merging it again

merged_img = cv.merge([b,g,r])
cv.imshow("Merged image" ,merged_img)

cv.waitKey(0)
cv.destroyAllWindows()