import cv2
import numpy as np

img = cv2.imread("Resource\Hue.JPG")
cv2.namedWindow("Canny Image", cv2.WINDOW_NORMAL) #Fixed Size Window

#Convert into Gray Scale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image",imgGray)
cv2.waitKey(0)

#Blur Image
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
cv2.imshow("Blur Image",imgBlur)
cv2.waitKey(0)

# #Edges
imgCanny = cv2.Canny(img, 255/3, 255)
cv2.imshow("Canny Image",imgCanny)
cv2.waitKey(0)

#Create kernel
kernel = np.ones((5,5), np.uint8)

#Dilation
imgDialte = cv2.dilate(imgCanny, kernel, iterations=1)
cv2.imshow("Dialation Image", imgDialte)
cv2.waitKey(0)

#Erosion
imgEroded = cv2.erode(imgDialte,kernel,iterations=1)
cv2.imshow("Erosion Image",imgEroded)
cv2.waitKey(0)
 



