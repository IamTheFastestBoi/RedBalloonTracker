import cv2
from utils import getTrackbarValue , getContours , initalizeTrackbars

cap = cv2.VideoCapture(0)

cv2.namedWindow("Video", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Video", 960, 540)  # Büyük kamera ekranı


initalizeTrackbars()

while True:
    success, img = cap.read()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # BGR -> HSV
    getTrackbarValue()
    lower , upper = getTrackbarValue()
    mask = cv2.inRange(imgHSV, lower, upper)
    getContours(mask , img)
    cv2.imshow("Video", img)
    cv2.imshow("Mask", mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
