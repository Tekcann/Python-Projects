# *****assignment operators*****

# x = 5
# y = 10
# z = 20

#ya da
x,y,z = 10,5,20

# değişkenlerin değerleri birbiri ile değişiyor
x,y = y,x 

# x in var olan değeri ile aynı değerin 5 fazlası x değişkenine yazılır
x = x + 5 
# ya da  ikiside aynı şey
x += 5

# diğer matematiksel işlemler
"""
x -= 5     #çıkarma
x *= 5     #çarpma
x /= 5     #bölme
x %= 5     #mod alma
x //= 5    #tam bölme işlemi kalansınz
x **= 5    #üs alma işlemi => veya x = y ** z falan
"""

"""
values = 1,2,3,4,5
print(values)
print(type(values))
#elemaların bilgilerini tek tek değişkenlerie yazdırabiliyoruz
#elemanlar ile değişkenlerin sayısı aynı olmalı

x,y,*z = values
# *z => yaptığımızda z bir diziye dönüşür 
# fazla olan elemanları kendi içerisine aktarır


print(x,y,z[1])
"""

# *****ATAMA OPERSTÖRLERİ UYGULAMAASII*****
"""
x, y, z, = 2, 5, 10

numbers = 1, 5, 7, 10, 6

# 1. soru
kullanici_işlem = int(input("Birinci Sayıyı Giriniz :")) * int(input("İkinci Sayıyı Giriniz: "))
# input değeri anında int değere dönüşebiliyor çok iyi
 
toplam = x + y + z
sonuc = kullanici_işlem - toplam
print(sonuc)

# 2. soru
sonuc = x // y
print(sonuc)

# 3. soru
print(toplam % 3)

# 4. soru
print(y ** x)

# 5. soru
x, *y, z = numbers
print(z ** 3)

# 6. soru
print(y[0] + y[1] + y[2])
"""


#********Comparisan Operators*******
#        Karşılaştırma Öperatörleri
# koşullar

"""
a, b, c, = 5, 5, 10

result = (a == b) # true  
result = (a == c) # false

password = "1234"
username = "Ahmet"

# bilgi doğruysa true değeri döner
# yanlışsa false değeri döner
result = ("ahmt" == username)
result = ("Ahmet" == username)

# eşit değil mi sorusunu sorar 
# buna mutakıp eşit değilde true olur 
# eşitse false olur
result = (a != b)
result = (a != c)

#ilk değerin ikinci değerden büyük mü diye sorar
result = (a > c)
#eşit veya büyükse
result = (a >= c)

#ilk değerin ikinci değerden KÜÇÜK MÜ sorusunu sorar
result = (a < c)
#eşit veya küçükse
result = (a <= c)

#True bilgisi 1 e eşittir
result = (True == 1)

#False değeri 0 a eşittir
result = (False == 0)

print(result)
"""

# *****KARŞILAŞTURMA Operatörleri UYGULAAISII******
"""#SIKICIIIIIII
#1. soru
s1 = int(input("Birinci Sayıyı Giriniz :")) 
s2 = int(input("İkinci Sayıyı Giriniz :"))
result = (s1 > s2)

print(f"{s1} {s2} den büyüktür : {result}")

#2. soru
vize1 = float(input("birinci vize notu :"))
vize2 = float(input("ikinci vize notu :"))
final = float(input("final notu :"))

ort =(((vize1 + vize2)/2) * 0.6) + (final * 0.4)

 
result = (ort >= 50)
print(f"ortalaman :{ort} sınıdı geçme durumun :{result}")
"""


#*****LOGİCAL OPERATORS*****
#MANTIK OPERATÖRLERİ
"""
#result = (5 <= x <= 10) .ör

x = 7
hak = 5
devam = "e"

            # **END** #
# İki Farkı Koşulunda doğru olması gerekir
result = (x > 5) and (x < 10) #true
result = (hak > 0) and (devam == "a")#false a değil e


            # **OR** #
# Sadece Bir Koşulun Doğru Olması Gerekir
result = (x > 0) or (x % 2 == 0)

            # **NOT** #
# Koşulun Doğruluna Değil Yanlış Oluşuna Bakar
# Eğer koşul YANLIŞ ise 'True' değerini gönderir
# Eğer Koşul DOĞRU ise 'False' değerini gönderir
result = not(x > 0)

#print(result)
"""


# ****Identy Operator: is****
"""
x = y =[1, 2, 3,]
z = [1, 2, 3,]
# koşul ifadeleri değer karşilasması yapar adres değil
print(x == y)
print(x == z)

# Tanımlanan objelerin tamamen aynı olmasını kontrol eder
print(x is y)
print(x is z)

x = [1, 2 ,3]
y = [1, 2 ,3]

print(x == y)# True üretiyor
print(x is y)# False üretiyor
print(x is not y)# True üretiyor
"""

#****Membership Operator: in****
"""
x = ["apple", "banana"]

# 'banana' elemanı x listesinde var mı?
print("banana" in x)

name = "Çınar"
# 'a' harfi name değişkenin içerisinde bulunnuyor mu?
print("a" in name)

#  'a' yok mu diye soruluyor
#yoksa True, varsa False
print("a" not in  name)
"""