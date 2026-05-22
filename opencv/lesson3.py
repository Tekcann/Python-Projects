import cv2
import numpy as np

cap = cv2.VideoCapture("videolar/yimek.mp4")

while(cap.isOpened()):
    ret, frame = cap.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("pencereee", grey)

    if(cv2.waitKey(1) == ord("q")):
        break

cap.release()
cv2.destroyAllWindows()
