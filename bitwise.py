import cv2 as cv
import numpy as np

blank = np.zeros((400,400s), dtype='uint8')

rec = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
cir = cv.circle(blank.copy(), (200, 200), 200, 255, -1)
# cv.imshow('Rectangle', rec)
# cv.imshow('Circle', cir)

# Bitwise And
bit_and = cv.bitwise_and(rec, cir)
cv.imshow('Bitwise_and', bit_and)

# Bitwise OR
bit_or = cv.bitwise_or(rec, cir)
cv.imshow('Bitwise_OR', bit_or)

# Bitwise XOR
bit_xor = cv.bitwise_xor(rec, cir)
cv.imshow('Bitwise_XOR', bit_xor)

# Bitwise NOT
bit_NOT = cv.bitwise_not(rec)
cv.imshow('Bitwise_NOT', bit_NOT)

cv.waitKey(0)
cv.destroyAllWindows()