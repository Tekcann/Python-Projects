import cv2
import numbers as np

cap = cv2.VideoCapture(0)

def cameraSetup():
    ret, frame = cap.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    return grey, frame

