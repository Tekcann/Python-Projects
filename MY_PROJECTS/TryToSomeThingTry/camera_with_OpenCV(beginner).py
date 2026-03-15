import cv2
import numpy as np

# hangi kamerayı kullanacağımı belitiyoruz
cap = cv2.VideoCapture(0)

while True:
    # kamera ansında süreklü olarak fotoğraf çekiyor ve biz bu fotoğrafı sürekli olarak 
    # ekrnadaki pencereye yansıtıyoruz bu sayede aslında bir video görüntüsü elde ediyoruz
    ret, frame = cap.read() 
    # ret => görüntü varmı (true, false)
    # frame => görüntünün kendisi

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # gelen görüntüyü HSV renk uzayına göre yeniden şeküllendiriyor

    cv2.imshow("frame", frame) # kamerada kendi görüntün gözükür
    cv2.imshow("HSV Penceresi", hsv_frame) #sen varsın ama sen değilsin gibi gözükür (HSV)

    # programları kapatmak için q tuşuna basılmasını bekliyor
    if(cv2.waitKey(1) & 0xFF == ord("q")):
        break


# kamerayı serbest bırakır (başka uygulamaların kullanması için gerekli)
cap.release()
# kod ile açılan bütün pencerelerin hepsini kapatır
cv2.destroyAllWindows()

