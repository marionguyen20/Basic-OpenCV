import cv2
import numpy as np 

img = cv2.imread ("Resource\doraemon.jpg")
cv2.namedWindow("Output", cv2.WINDOW_AUTOSIZE)

width = 230
height = 345

#Points of 4 corners
pts1 = np.float32([[1015,284],[1248,281],[1016,628],[1251,628]])

#Reference points
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

#Transform matrix
matrix = cv2.getPerspectiveTransform (pts1, pts2)

#Output image
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Output", img)
cv2.imshow ("Image",imgOutput)
cv2.waitKey (0)