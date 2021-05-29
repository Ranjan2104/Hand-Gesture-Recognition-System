# Developed by Amresh Ranjan.

import cv2
import numpy as np

hand = cv2.imread('hand2.jpg', 0)

ret, the = cv2.threshold(hand, 70, 255, cv2.THRESH_BINARY)

contours, hierachy = cv2.findContours(the.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

hull = [cv2.convexHull(c) for c in contours]

final = cv2.drawContours(hand, hull, -1, (250,0,0))

cv2.imshow('Original Image', hand)
cv2.imshow('Thres Image', the)
cv2.imshow('Convex Hull', final)

cv2.waitKey(0)
cv2.destroyAllWindows()
