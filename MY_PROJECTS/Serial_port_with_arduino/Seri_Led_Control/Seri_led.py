# kütüphaneleri kuruyoruz
import serial
import serial.tools.list_ports
import time

# bilgisayarda bağlı portları değişkene aktarır
ports = serial.tools.list_ports.comports()


print("Portlar taranıyor...")
print("*" * 30)

# döngü ile alınan portlar sırayla ekrana yazdırılır
for port in ports:
    print(f"PORT: {port.device} | Tanım: {port.description}")

#kullanıcı seçtiği portu yazar ve bu pot ile seri haberleşme yapılır
try:
    COM = input("Lütfen Kullanmak İstediğiniz Portu Giriniz: ")
    COM = COM.upper().strip()# gönderilen metni her harfini büyük yapar ve boşlukları siler
except Exception as ex:
    print("hata: " + ex)


# bir nesne oluşturuyoruz ve nesnenin özelliklerini belirliyoruz
arduino = serial.Serial(port=COM, baudrate=9600, timeout=.1)

# ardunoya veri gönderek fonksiyon komutları
def led_kontrol(command):
    arduino.write(bytes(command, "utf-8"))
    # gelen veri "write" komutu ile seri porta yazılır
    # veriler bytes olarak gönderilmeli ve utf-8 olmalı(türkçe karakterler için)
    time.sleep(0.05)

print("Led di yakıp söndürmek için 1 veya 0 basınız")

while True:# işlemi döngüye alıyoruz
    command = input("Komut: ")
    led_kontrol(command)
    # kullanıcan gelen veri led_kontrol fonksiyonuna gider 
    # ve işlemleri yapr