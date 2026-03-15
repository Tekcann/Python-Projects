# kütüphaneleri kuruyoruz
import serial
import serial.tools.list_ports
import time

# bilgisayarda bağlı portları değişkene aktarır
ports = serial.tools.list_ports.comports()


print("Portlar taraniyor...")
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

#seri porttan veri okuma işlemleri
def serRead():
    ham_veri = arduino.readline().decode("utf-8").rstrip()
    # arduinodan gelen ham veriyi temizliyoruz
    zaman = time.strftime('%Y-%m-%d %H:%M:%S')
    # gerçek zamanı almak için gerekli işlemler
    time.sleep(0.5)
    if(len(ham_veri) > 2):
        # aldığımız verileri kayıt için uygun hale getiriyoruz
        return f"{zaman} => Nem: {ham_veri.split(',')[0]}, Sıcaklık {ham_veri.split(',')[1]} derece\n"
    else:
        print(f"hatalı veri atlandı {ham_veri}")
        return " "
    

# hazır olan veriyi dosyaya kayıt eden fonksiyon
def kayitEt(kayit):
    with open("sensor_verileri", "a" , encoding="utf-8") as file:
        print(kayit)
        file.write(kayit)
        file.flush()


# sürekli devam etmesi ve fonksiyonların çağrılma işlemleri
try:      
    while True:
        kayit = serRead()
        kayitEt(kayit)
except Exception as e:
    print(e)