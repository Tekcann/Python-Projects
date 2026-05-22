import cv2
import numpy as np


picture = cv2.imread("resimler/sad-cat-2.jpg", 0)
cv2.imshow("Resim", picture)

cv2.imwrite("resimler/grey-sad-cat.png", picture) #resmi kaydeder 
# (dosya yolu yazmazsan aynı klasöre kaydeder)

a = cv2.waitKey(0)

if( a == ord("q")):
    cv2.destroyAllWindows()

elif a == ord("s"):
    cv2.imwrite("resimler/grey-sad-cat.png", picture) #resmi kaydeder 
    # (dosya yolu yazmazsan aynı klasöre kaydeder)

