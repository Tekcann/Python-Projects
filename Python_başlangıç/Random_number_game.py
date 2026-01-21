# SAYI TAHMİN OYUNU
import random
rnd_sayi = random.randint(0, 100)

puan = 100

deneme_hakki = float(input("Kaç Deneme Hakkınız Olsun :"))
hasar = puan / deneme_hakki

while (True):
        
    kullanici_sayi = int(input("Tahmin ettiğiniz sayıyı giriniz :"))
    if(kullanici_sayi == rnd_sayi):
        kazandiniz_mesaji = "Tebrikler KAZANDINIZ"
        print(kazandiniz_mesaji.center(32, "*"))
        print(f"Sayı :{rnd_sayi}, Aldığınız puan :{puan}")
        break

    else:
        puan -= hasar
        if(kullanici_sayi < rnd_sayi):
            print(f"{kullanici_sayi} Sayısından Daha Yüksek Bir Değer Giriniz")

        else:
            print(f"{kullanici_sayi} Sayısından Daha Küçük Bir Değer Giriniz")

    if(puan <= 0):
        kaybettin_mesaji = "PUHHH YAZIKLAR OLSUN"
        print(kaybettin_mesaji.center(32, "*"))
        break

print(f"hasar :{hasar}, rndSayı :{rnd_sayi}, puan :{puan}")


# Girilen Sayının Asal Olup Olmadığını bulalım

while (True):

    girilen_sayi = int(input("Bir Sayı Giriniz :"))
    for i in range(2, girilen_sayi):
        
        if(girilen_sayi % i == 0):
            print("Sayı asal değil")
            break
        else:
            print("Sayı ASAL dirrr")
            break
