# DİZİLERİN İÇİNDE FOR VE YA İF_ELSE İŞLEMLERİNİ YAPABİLİRSİN
# BU BÜYÜÇÜ İŞİ VAYYY BE

numbers = []

for x in range(10):
    numbers.append(x)
print(numbers)

# bu iki kod bloğu yanı işleve sahip

numbers =[(x) for x in range(10)]
print(numbers)

#*******************************************

for x in range(10):
    print(x**2)

#bu iki kod bloğuda ayı işlevi yapar 
#aşağıdaki dizinin içine yerleştirir

numbers = [(x**2) for x in range(10)]
print(numbers)

#********************************

# o ile 10 arasındaki değerleri kendisi ile çarpar
# ve sonucun mod 3 ü 0 ise dizinin içine yerleştirir
# koşulu karşıamıyorsa eleman dizinin içine giremez
 
numbers = [(x*x) for x in range(10) if x % 3 == 0]
print(numbers)

#******************************************

myString = "Hello"
myList = []

for latter in myString:
    myList.append(latter)
print(myList)

# İKİSİDE AYNI İŞLEVE YARIYOR

myList = [(latter) for latter in myString]
print(myList)

#********************************************

# var olan listeye işlem yaparak sonucu yeni listeye
# ekleyebiliyoruz
years = [1983,1999,2008,1956,1986]
ages = [(2026 - year) for year in years ]

print(ages)

#*******************************************
# Önemli Not: Eğer dizide işlem yapacaksak
# ve else komutu kullanılacaksa bu koşul ilk olarak yazılmalı
# ama oluşturduğumuz koşulu sadece if ten oluşuyor ise bu koşulu
# döngülerin arkasına da yazabiliriz
# AMA GENE DE BİZ HEP İLK PARAMETRA OLARAK KOŞUL YAPISINI KULLANALIM 

result = [(x) if x % 2 == 0 else "TEK" for x in range(1, 10)]
print(result)

#*********************************************

#DÖNGÜ İÇİNDE DÖngü

result = []
for x in range(3):
    for y in range(3):
        result.append((x, y))
print(result)

# ikiside aynı kapıya çıkıyor

# not: ilk yazdığımız parametra diğer parametreyi içine alıyor
# yani y döngüsü x döngüsünün içinde 
numbers = [(x,y,z) for x in range(3) for y in range(3) for z in range(3)]
print(numbers)

