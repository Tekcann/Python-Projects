# ***///***FORRR***///***
numbers = [1,2,3,4,5]
"""
#dizideki bütün sayıları yazdırma
for num in numbers:
    print("Merhaba Dünya")
#num yerine istediğin yazılabilir
#numbers => dizideki eleman sayısı kadar tekrar eder

names = ["çınar", "sadık", "sena", "ahmet"]

for name in names:
    print(f"my name is {name}")

name = "Ahmet Tekcan"

for n in name:
    print(n)

#NOT: Pythonda her bir string ifade bir dizi mantığı ile çalışır

tuple = [(1,2),(3,4),(5,6)]
#ikili olunca yazım şekline göre 
# a ve b birinci ve ikinci değerleri alır
for a,b in tuple:
    print(a,b)

d = {"k1" : 1, "k2" : 2, "k3" : 3}
#key bilgilerini alıyor
for item in d:
    print(item)

#eger değerlere ulaşmka istersek
for item in d.items():
    print(item)

#eger iki değeride ayrı ayrı istersek
for key,value in d.items():
    print(key, value)
"""

# ***FOR DÖNGÜSÜ UYGULAMASI***
sayilar = [1,3,5,7,9,12,19,21]

# 1. soru
"""
kat3 = 0
for sayi in sayilar:
    if(sayi % 3 == 0):
        kat3 +=1
print(kat3)
"""

# 2. soru
"""
toplam = 0
for sayi in sayilar:
    toplam += sayi

print(toplam)
"""

# 3. soru
"""
for sayi in sayilar:
    if(sayi % 2 == 1):
        print(sayi ** 2)
"""
sehirler = ["kocaeli", "istanbul", "ankara", "izmir", "rize"]

# 4. soru

for sehir in sehirler:
    if(len(sehir) <= 5):
        print(sehir)
    else:
         print("a")

urunlar =[
    {"name":"samsung s6", "price" : "3000"},
    {"name":"samsung s7", "price" : "4000"},
    {"name":"samsung s8", "price" : "5000"},
    {"name":"samsung s9", "price" : "6000"},
    {"name":"samsung s10", "price" : "7000"}
]

# 5. soru

toplam = 0
for urun in urunlar:
    print(urun["price"])
    toplam += int(urun["price"])

print(toplam)

# 6. soru

for urun in urunlar:
    fiyat = int(urun["price"])
    if(fiyat <= 5000):
        print(urun["name"])



# ***///***WHİLEEEE***///***

# 1-100 e kada

x = 1

while(x <= 100):
    if( x % 2 == 1):
        print(f"Sayı TEK {x}")
    else:
        print(f"Sayı ÇİFT {x}")
    x += 1


#değişkenin içinde hiçbirşey yoksa 
name = "" # False değer üretir. Boşlukta bir karakterdir!!!


#kok içerisinde baştsn ve sondan boşlukları silersek
#.strip()
while not name.strip():
    name = input("isminizi Gİrin :")

print(f"Merhaba {name}")


# ***---UYGULAMALAR---***

sayilar = [1,3,5,7,9,12,19,21]

#1. soru

x = 0
while (x < len(sayilar)):
    print(sayilar[x])
    x += 1


#2. soru

start_value = int(input("Başlangıç Değerini Giriniz :"))
finish_value = int(input("Bitiş Değerini Giriniz :"))

while (start_value <= finish_value):
    print(start_value)
    start_value += 1


#3. soru

x = 100

while ( x > 0):
    print(x)
    x -= 1


#4. soru

numbers = []
x = 0
while(x < 5):
    print(f"Girilmesi gereken Sayı miktarı {5 - x}")
    sayi = int(input("Bİr Sayı Giriniz :"))
    numbers.append(sayi)   
    x += 1

numbers.sort()

print(numbers)


# bubble sort with while

y = 0
while ( y < len(numbers)):
    z = 0
    while (z < len(numbers) - y - 1):
        if(numbers[z] > numbers[z + 1]):
           numbers[z], numbers[z + 1] = numbers[z + 1], numbers[z] 
        z += 1
    y += 1
print(numbers)



#5. soru

urunler = [
    {"name" : "price"},
    
]
urunler = {}
urun_sayisi = int(input("Ürün Sayısını Giriniz :"))
i = 0
while (i < urun_sayisi):
    name = (input("Ürünğn Adını Giriniz :"))
    price = (input("Ürünğn Fiyatını Giriniz :"))
    
    urunler[i]  = {
        "name" : name,
        "price" : price,
    }
    i += 1     

print(urunler)
