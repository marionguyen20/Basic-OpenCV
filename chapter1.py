import cv2 


#Read Image
img = cv2.imread("Resource/Hue.JPG")
cv2.namedWindow('Output', cv2.WINDOW_NORMAL) #Fixed Sized image
cv2.imshow("Output",img)
cv2.waitKey(0)


#Read Video

#Create video capture object
cap = cv2.VideoCapture("Resource\MusicVideo.mp4")

#Display
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(15) & 0xFF == ord('q'):
        break

#Read Webcam

#Create video capture object
cap = cv2.VideoCapture(0)
cap.set(3, 640) #Set width
cap.set(4, 480) #Set height
cap.set(10, 100) #Set brightness

#Display
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(15) & 0xFF == ord('q'):
        break
