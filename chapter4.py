import numpy as np 
import cv2

#Create matrix of 0
img = np.zeros ((512,500,3), np.uint8)
print (img.shape)

# #Color whole image
img[:] = 255,0,0

#Color range
img[200:300, 100:300] = 105,150,200

#Draw line
cv2.line (img, (0,0), (img.shape[1],img.shape[0]),(0,255,0),5)

#Draw Rectangle
cv2.rectangle (img, (10,10), (250,200),(28,4,200),3)

#Draw circle
cv2.circle (img, (250,250),100,(255,0,0),3)

#Text
cv2.putText (img, "Hello World", (300,150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 3)

cv2.imshow ("Image",img)
cv2.waitKey(0)
