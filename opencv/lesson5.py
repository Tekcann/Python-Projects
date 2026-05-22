import cv2
import numpy as np

img = cv2.imread("resimler/Sinek.png", 0)

#kare için başlangıç ve bitiş noktaları girilir
img2 = cv2.rectangle(img, (10,10), (210,220), (0, 255, 0), 5)

#daire çizerken once orjin ardından çap değeri yazılır
img3 = cv2.circle(img, (110,115), 40, (0, 0, 255), -1)
# herhangibir şekiln içi dolu olsun istiyorsak kalınlık parametrasi -1 olmalı

font = cv2.FONT_HERSHEY_COMPLEX
img4 = cv2.putText(img3, "DENEME", (20, 135), font, 1, (255, 255, 255), 1, cv2.LINE_AA)



cv2.imshow("sasdfghjsinek", img4)

if(cv2.waitKey(0) == ord("q")):
    cv2.destroyAllWindows()