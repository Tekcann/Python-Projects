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


# *******************UYGULAMALAR******************

# 1. soru
def yazdir(kelime, tekrar):
    i = 0   
    while i < tekrar:
        i += 1
        print(kelime)
    #ya de
    print(kelime * tekrar)

yazdir("adana", 10)

# 2. soru
def listeleme(*dizi):
    liste = []
    
    for list in dizi:
       liste.append(list)
    return liste

result = listeleme(2,3,45,6,7,8,9,35)
print(result)

# 3. soru

def aralarindakiAsallar(s1,s2):    
    for s in range(s1,s2 + 1):
        if (s > 1):
            for i in range(2, s):
                if (s % i == 0):
                    break
            else:
                print(s)
# else döngüler ilede kullanıla bilir ve 
# döngü içerisinde break komutu kullanılmazsa else içerisinde yazılan çalışır
# gibi birşey anladım

# not: Döngüdeki else, "Eğer döngü hiçbir break komutuna çarpmadan 
# doğal bir şekilde bittiyse çalış" anlamına gelir.

sayi1 = int(input("Birinci Sayıyı Giriniz :"))
sayi2 = int(input("İkinci Sayıyı Giriniz :"))
aralarindakiAsallar(sayi1, sayi2)

# 4. soru

def tamBolenleri(sayi):
    tamBolenler = []

    for i in range(2, sayi):
        if (sayi % i == 0):
            tamBolenler.append(i)
    return tamBolenler

print(tamBolenleri(20))


# ******************LAMBDA EXPRESSİON*******************
# ******************************************************

# WİTHOUT LAMBDA 
def square(num): return num ** 2
result = square(2)

print(result)

numbers = [1,3,5,9,10,12,13,14,156,67,72,8]

# numbers dizisinin her bir elemanının karesini almak stiyoruz. ama neden

# dizi içerisinde ki her bir elemana ulaşıp 
# bir fonksiyon üzerinden geçirebiliriz

# dizideki elemanlar squqre fonkisoyuna gidiyor 
# ve return ile gelen değerler list fonksiyonu ile 
# listeye çevriliyor
result = list(map(square, numbers))
print(result)

# dizideki bütün elemanlar geziliyor square fonkiyonu çalışıyor
# ve sırayla ekrana yazılıyor

for item in  map(square, numbers):
    print(item)


###************ WİTH LAMBDA ******************
# ********************************************

# NOT:!! map ifadesi dizinin her bir elemanını bir fonksiyona gönderme işlemi yapan bir fonksiyon !!

# Bir fonksiyon tanımlayıp çağırmak yerine 
# anlık olarak lambda komutu ile fonksiyon oluşturabiliyoruz

# oluşan işlemler bir dizi haline getiriliyoe ve ekrana yazdırılıyor

result = list(map(lambda num: num ** 2, numbers))
print(result)

# dizinin her bir elemanına sırayla oluşan fonksiyon yazılıyor 
# ve sırayla ekrana yazdırılıyor
for item in  map(lambda num: num ** 2, numbers):
    print(item)

# ****************
print("*" * 50)
# lambda ifadesini bir değişkene atayabiliriyoruz
square3 = lambda num: num ** 2

result = square3(3)
print(result)

# return komutuna koşul ekledik bu sayede
# %2 si 0 a eşit olmayanlar geri gönderilemedi sanırım

# def chack_even(num): return(num % 2 == 0)
chack_even = lambda num:num % 2 == 0

#filter komutu True False üretir bir koşula bağlıdır
# eğer koşul doğruysa dizinin içindeki elemanı alır
# eğe koşulu karşılamıyorsa elemanı eler ve kullandırtmaz
#bir süzgeç görevi görür belli koşula oygun olanların geçmesine izin verir (10 dan büyükmü, 5 ten büyük bütün sayılar al gibi koşullar için yugundur mod falan işte)
# map fonksiyonu bir her bir elemana etki eder ve formunu değiştirir (karesini alır yada ikiye böler string yapar vb)
result = list(filter(chack_even, numbers))
print(result)









