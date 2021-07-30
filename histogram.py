import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread('Valorant.png')

# Grayscale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Grayscale Histogram

hist = cv.calcHist([gray], [0], None, [256], [0,256])
# cv.imshow("Histogram_gray", hist)


plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('No. of pixels')
plt.plot(hist)
plt.xlim([0, 256])
plt.show()


plt.figure()
plt.title('Coloured Histogram')
plt.xlabel('Bins')
plt.ylabel('No. of pixels')
colors = ('b', 'g', 'r')

# Color histogsrm 
for i,col in enumerate(colors):
    color_hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(color_hist, color=colors)
    plt.xlim([0, 256])

plt.show()

cv.waitKey(0) 
cv.destroyAllWindows()
