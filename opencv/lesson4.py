import cv2
import numpy as np

# 512 ye 512 pixel arka pilen oluştruduk 
# (numpy kütüpahesi ile matriks oluştursuk)
img = np.zeros((512,512,3), np.uint8)

#çizgi için değerler sırasıyla: 
# başlangıç konumu (X,Y), bitiş konumu(X,Y) 
# rengi (mavi, yeşil, kırmızı), kalınlığı (sayı)
img2 = cv2.line(img, (0,0), (512,512), (255, 0, 0), 6)
# by komut direk olarak resmi değiştiriyor


cv2.imshow("pespencere", img2)
# ikisindede aynısı oluyor
cv2.imshow("epencere", img)

if(cv2.waitKey(0) == ord("q")):
    cv2.destroyAllWindows()