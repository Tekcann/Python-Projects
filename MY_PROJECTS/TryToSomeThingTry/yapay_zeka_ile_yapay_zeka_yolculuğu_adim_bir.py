import time

class Motor:
    def __init__(self, speed, temperature):
        self.speed = speed
        self.temp = temperature
        self.is_activate = True

    def speed_add(self):

        if (self.temp >= 80 ):
            print("Motor Aşırı Isındı")
            self.is_activate = False
        else:
            
            if(self.speed >= 100):
                self.temp += 5
                print(f"Sıcaklık 5 arttı  şuan: {self.temp}")
            else:
                self.speed += 10 
            print(f"hız 10 arttı şuan: {self.speed}") 

try:
    motor1 = Motor(10,5)
    while motor1.is_activate:    
        motor1.speed_add()
        time.sleep(0.5)

except Exception as e:
    print("hata: " + e)







