import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while (True):
    ret, frame = cap.read()
    cv2.imshow("pencere adı", frame)
    
    if(cv2.waitKey(1) == ord("q")):
        cap.release()
        cv2.destroyAllWindows()

