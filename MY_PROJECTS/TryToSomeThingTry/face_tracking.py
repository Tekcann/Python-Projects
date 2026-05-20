import cv2
import numpy as np

cap = cv2.VideoCapture(1)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def cameraSetup():
    ret, frame = cap.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    

    

    return grey, frame
 
def facesTrack(grey, frame):
    faces = face_cascade.detectMultiScale(grey, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(frame, "biri", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    

    
    
while True:
    grey, frame = cameraSetup()
    facesTrack(grey, frame)
    


    cv2.imshow("frame", frame)
    cv2.imshow("greyFrame", grey)

    if(cv2.waitKey(1) & 0xFF == ord("q")):
        break

cap.release()
cv2.destroyAllWindows()


