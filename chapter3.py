import cv2

#Read Image
img = cv2.imread("Resource\Hue.JPG")

#Resize
#print(img.shape) #Find the current size
imgResize = cv2.resize (img, (1500,1024))
#cv2.imshow("Output", imgResize)

#Crop
imgCrop = img[0:200,200:500]
print(imgCrop.shape)

cv2.imshow("Crop Image", imgCrop)

cv2.imshow("Original Image", img)

cv2.waitKey(0)
