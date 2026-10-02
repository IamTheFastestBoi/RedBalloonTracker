import cv2
from stackImages import stackImages
import numpy as np

def getContours(img , imgContour):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            perimeter = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * perimeter, True)
            objCor = len(approx)
            if objCor > 8:
                x, y, w, h = cv2.boundingRect(cnt)
                circularity = ( 4 * 3.14 * area) / (perimeter * perimeter)
                aspRatio = float( w / h )
                if circularity > 0.65 or  1.3 > aspRatio > 0.7:
                    cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 2)

def initalizeTrackbars():
    def empty(a):
        pass

    cv2.namedWindow("BGR(original)")
    cv2.resizeWindow("BGR(original)", 600, 400)
    cv2.createTrackbar("Hue Min", "BGR(original)", 0, 179, empty)
    cv2.createTrackbar("Hue Max", "BGR(original)", 179, 179, empty)
    cv2.createTrackbar("Sat Min", "BGR(original)", 0, 255, empty)
    cv2.createTrackbar("Sat Max", "BGR(original)", 255, 255, empty)
    cv2.createTrackbar("Val Min", "BGR(original)", 0, 255, empty)
    cv2.createTrackbar("Val Max", "BGR(original)", 255, 255, empty)

def getTrackbarValue():
    h_min = cv2.getTrackbarPos("Hue Min", "BGR(original)")
    h_max = cv2.getTrackbarPos("Hue Max", "BGR(original)")
    s_min = cv2.getTrackbarPos("Sat Min", "BGR(original)")
    s_max = cv2.getTrackbarPos("Sat Max", "BGR(original)")
    v_min = cv2.getTrackbarPos("Val Min", "BGR(original)")
    v_max = cv2.getTrackbarPos("Val Max", "BGR(original)")
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    return lower , upper








