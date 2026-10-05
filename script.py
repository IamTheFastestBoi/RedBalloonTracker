import cv2
from utils import getTrackbarValue , getContours , initalizeTrackbars
import numpy as np

cap = cv2.VideoCapture(0)

cv2.namedWindow("Video", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Video", 960, 540)  # Büyük kamera ekranı


initalizeTrackbars()

while True:
    success, img = cap.read()
    imgBlur = cv2.GaussianBlur(img, (7, 7), 0)
    imgHSV = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2HSV) # BGR -> HSV
    lower , upper = getTrackbarValue()
    mask = cv2.inRange(imgHSV, lower, upper)
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.dilate(mask, kernel, iterations=1)
    mask = cv2.erode(mask, kernel, iterations=1)
    getContours(mask , img)
    cv2.imshow("Video", img)
    cv2.imshow("Mask", mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
