# ***Metot***
#  Metot bir class ın içindedir
# eğe nokta koyarak çalışıyorsa o metotodur
# classların içinde olarak nitelendirilir
list = [1,2,3]

list.append(4) # append bir metot
list.pop() # pop bir metot

print(list)

# ***fonksiyon***
# Başıboştur. Bir nesneye ait değildir.
# (Örn: print(), len())

# Parantesin içine bir parametre yazarız şart değil
def sayHello(name = "user"):
   return (f"Hello {name}")
# Hazırlanan işlemi çağrıldığı yere geri gönderir
# istersen direk kulllan istersen bir değişkene kaydet
# ÖRNEKLER: print() - input() - len() - type() 

msg = sayHello("Ada")

print(msg)
print(sayHello("Çınar"))

def total(num1, num2):
   return num1 + num2

result = total(10, 20)
result = total(30, 56)
print(result)


#****************************
def yasHesapla(dogumYili):
   return 2026 - dogumYili

ageCınar = yasHesapla(2017)
ageAhmet = yasHesapla(2009)
ageAda = yasHesapla(1999)

print(ageCınar, ageAhmet, ageAda)

#************************************

def EmekliligeKacYilKaldi(dogumYili, isim):
    """
    DOCSTRIG: Doğum yılınıza göre emekliliğe kaç
    yıl kaldı
    INPUT: Doğum Yılı
    OUTPUT: Hesaplanan yıl
    """
    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas
    if( emeklilik > 0):
      print(f"emekliliğine {emeklilik} yıl kaldı")
    else:
      print("zaten emeklisiniz")

EmekliligeKacYilKaldi(2009 , "Ahmet")
EmekliligeKacYilKaldi(1999 , "Süleyman")
EmekliligeKacYilKaldi(0 , "Fahrettin")

print(help(EmekliligeKacYilKaldi))

def changeName(n):
    n = "ada"

name = "yiğit"

changeName(name)
# isim değişmedi çünkü adresleri farklı
print(name)

def change(n):
    # adres kopyalanıyor ve
    # adreste değişiklik yapılıyor bu 
    # sebeple değişiklik ikisinde de oluyor
    n[0] = "İstanbul"

# 0 ıncı index değişiyor
sehirler = ["Ankara", "İzmir"]

#Bu kısımda sehirler dizsinin her bir elemanı n dizisine kopyalanır
n = sehirler[:]

n[0] = "Adanaa"
print(n)
print(sehirler)
print("*" * 50)
# Bu kısımda şehirler dizisi ile n dizisi aynı adresi alır 
# ve birinde yapılan değişikli diğerini etkiler
n = sehirler

n[0] = "Ankara"
print(n)
print(sehirler)
print("*" * 50)

# n ile sehirler dizisinin adresi aynı olunca
# ikisininde ismini birbirlerine karışık kullanılabiliyor
# change fonksiyonu içinde buluna n dizisinin sıfıncı elemanını 'istanbul' ypar
# adresler aynı olduğu için sehirler dizisininde ilk elemanı 'istanbul olur'
change(sehirler)

print(sehirler)
print(n)

# Bir dizi bilgisinin geleceğini belirtek için
# parametrenin öncesine '*' işareti konuyor
def add(*params):
    # print(params)
    # print(params[1])
    # return sum((params))
    sum = 0
    for n in params:
        sum += n
    return(sum)

print(add(10,20))
print(add(10,20,50))
print(add(10,20,54,96,9,85,852,0))

# #+***************************************

# Bir sözlük bilgisinin geleceğini belirmek için
# parametrenin başına '**' işareti konuyor

def displayUser(**args):
    for key, value in args.items():
        print(f"{key} is {value}")

displayUser(name = "Çınar", age = 2, city = "istanbul")
displayUser(name = "Ada", age = 12, city = "kocaeli", phone = "123456789")
displayUser(name = "Yiğit", age = 14, city = "ankara", phone = "987654321")


def myFunch(a, b, *arng, **kwargs):
    print(a)
    print(b)
    print(arng)
    print(kwargs)

myFunch(10, 20, 30, 40, 50, key1 = "value 1", key2 = "Value 2")


#*******************UYGULAMALAR******************

#1. soru