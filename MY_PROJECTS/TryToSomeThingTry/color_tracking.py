import cv2
import numpy as np
import math

# hangi kamerayı kullanacağımı belitiyoruz
cap = cv2.VideoCapture(0)

def camera_setup():
    # kamera ansında süreklü olarak fotoğraf çekiyor ve biz bu fotoğrafı sürekli olarak 
    # ekrnadaki pencereye yansıtıyoruz bu sayede aslında bir video görüntüsü elde ediyoruz
    ret, frame = cap.read() 
    # ret => görüntü varmı (true, false)
    # frame => görüntünün kendisi
   
    min_blue = np.array([100,140,17]) # H, S, V en alt limit 
    max_blue = np.array([140,255,255]) # H, S, V en üst limit

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    return cv2.inRange(hsv_frame, min_blue, max_blue), frame

def center_point(mask, frame):
    kernel = np.ones((5,5), np.uint8)

    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    M = cv2.moments(mask)

    if (M["m00"] != 0):
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])

    
        cv2.circle(frame, (cX, cY), 10, (0,255,0), -1)
        cv2.putText(frame, f"Hedef: {cX}, {cY}", (cX - 20, cY-20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        return cX, cY, M["m00"]
    else:
        return None, None, None

def direction_control(cX, cY, frame):

    height, width, _ = frame.shape

    center_x = int(width / 2)
    center_y = int(height / 2)

    cv2.line(frame, (center_x - 20, center_y), (center_x + 20, center_y), (0, 0, 255), 2)
    cv2.line(frame, (center_x, center_y - 20), (center_x, center_y + 20), (0, 0, 255), 2)


    hata_yatay = cX - center_x
    hata_dikey = cY - center_y

    mesafe = math.sqrt(hata_yatay**2 + hata_dikey**2)

    if(mesafe < 25):
        cv2.putText(frame, "Nesne Merkezde",(10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    return center_x, center_y

def get_motor_cammands(cX, cY, center_x, center_y, mevcut_alan, frame):
    error_x = cX - center_x
    error_y = cY - center_y

    hedef_alan = 1000
    hedef_alan = hedef_alan - mevcut_alan
    kp_ileri = 0.0001

    speed_ileri = hedef_alan * kp_ileri


    kp = 0.005

    speed_yatay = error_x * kp
    speed_dikey = error_y * kp

    speed_yatay = max(min(speed_yatay, 1.0), -1.0)
    speed_dikey = max(min(speed_dikey, 1.0), -1.0)
    speed_ileri = max(min(speed_ileri, 1.0), -1.0)

    cv2.putText(frame, f"Donus Gucu: {speed_yatay:.2f}, Yakinlik: {speed_ileri:.2f}",(10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    return speed_yatay, speed_dikey


while True:
    try:
        mask, frame = camera_setup()
        cX, cY, n = center_point(mask,frame)

        if(cX is not None) and (cY is not None):
            center_x, center_y = direction_control(cX, cY, frame)
            speed_x, speed_y = get_motor_cammands(cX, cY, center_x, center_y, n, frame)
        
        else:
            cv2.putText(frame, "Nesne Araniyor", (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        cv2.imshow("HSV Penceresi", mask)
        cv2.imshow("frame", frame)

        if(cv2.waitKey(1) & 0xFF == ord("q")):
            break
    except Exception as e:
        pass

        


cap.release()
cv2.destroyAllWindows()