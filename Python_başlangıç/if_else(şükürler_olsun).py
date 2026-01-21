username = "Ahmet"
password = "12345678"

# Koşullllllllsaaaaaaaaaarrrrrrrrr Sonundaa
"""
if (username == "Ahmet"):
    if (password == "12345678"):
        print("Merhaba Dünya")
    else:
        print("Şifren yanlış")
else:
    print("İsmin yanlış")
"""

#**** else-if ****
"""
x = 10
y = 20
if (x > y):
    print("x y den büyük")
elif (x == y):
    print("x y ye eşit")
else :
    print("y x den büyük")
"""
"""
num = int(input("sayı :"))

if (num > 0):
    print("Sayı pozitif")
elif (num < 0):
    print("Sayı negatif")
else:
    print("Sayı sıfır")
"""

# *****UYGULAMALAR*****

#1. soru
"""
name = input("İsminiz :")
age = int(input("Yaşınız :"))
education = input("Eğitim düzeyiniz :")

education = education.lower().strip()

if((age >= 18) and ((education == "üniversite") or (education == "lise")) ):
    print("EHliyet AlaBilirsiN")
else:
    print("ehliyet alamazsın")
"""

#2. soru
"""
not1 = int(input("Birinci not :"))
not2 = int(input("ikinci not :"))
sozlu = int(input("Sözlü not :"))

ort = (not1 + not2 + sozlu ) / 3

if(ort >= 0) and (ort <= 24):
    print(f"ortalaman :{ort} değerin 0 ")

elif(ort >= 25) and (ort <= 44):
    print(f"ortalaman :{ort} değerin 1 ")

elif(ort >= 45) and (ort <= 54):
    print(f"ortalaman :{ort} değerin 2 ")

elif(ort >= 55) and (ort <= 69):
    print(f"ortalaman :{ort} değerin 3 ")

elif(ort >= 70) and (ort <= 84):
    print(f"ortalaman :{ort} değerin 4 ")

elif(ort >= 85) and (ort <= 100):
    print(f"ortalaman :{ort} değerin 5 ")
"""
#3. soru
"""
from datetime import datetime

arac_tarihi = input("aracinizi trafiğe çıkış tarihi nedir\n(örnek: 2000.12.01) :")
arac_tarihi = arac_tarihi.split(".")
su_an = datetime.now()
tarih = datetime(int(arac_tarihi[0]), int(arac_tarihi[1]), int(arac_tarihi[2]))
servis_zamani = su_an - tarih
print(servis_zamani.days ,"Gün")

if(servis_zamani.days > 0) and (servis_zamani.days <= 365):
    print("1. Bakım yılı")

elif(servis_zamani.days > 365) and (servis_zamani.days <= 365*2):
    print("2. Bakım yılı")

elif(servis_zamani.days > 365*2) and (servis_zamani.days <= 365*3):
    print("3. Bakım yılı")

else:
    print("Maşallah araban çok eski")
"""

#4. soru 
"""
sayi = int(input("Sayı Giriniz :"))

if( 0 < sayi < 100):
    print(f"Sayı 0 ile 100 arasında {sayi}")
else:
    print(f"Sayı 0 ile 100 arasında değil {sayi}")
"""

# 5. soru
"""
sayi = int(input("Bir Sayı Giriniz :"))

if(sayi >= 0):
    if(sayi % 2 == 0):
        print("Sayı Hem Pozitif Hem de Çift Bir Sayı")
    else:
        print("Sayı Pazitif Tek Bir Sayı")
else:
    print("Sayı negatif bir sayı")
"""

# 6. soru
"""
email = "deneme@gmail.com"
password = "abc123"

kullanici_email = input("email giriniz :")
kullanici_password = input("Şifrenizi giriniz :")

if(kullanici_email == email):
    if(kullanici_password == password):
        print("Giriş Yapabilirsiniz")
    else:
        print("Şifre Yanlış")
else:
    print("Email Yanlış")
"""


