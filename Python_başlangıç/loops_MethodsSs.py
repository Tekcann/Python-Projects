# ---range() metodu---
# Bu metot range(başlat, durdur, artış miktarı)
# ya da sadece işimize yarayan kısmı yazabiliriz
"""
for item in range(50,100,10):
    print(item)

print(list(range(50,100,10)))
"""

# ---enumerate metodu---
# her kullanımda elemanın index ini ve değerini alır
# bir tuple tipine dönüştürür (0, "H") gibi
#

index = 0
greeting = "Hello World"

# enumerate' siz kullanım 
"""
for latter in greeting:
    print(f"index :{index} letter :{latter}")
    print(f"index :{index} letter :{greeting[index]}")
    index += 1
"""
# enumerate ile kullanım
"""
for item in enumerate(greeting):
    print(item)

for index, latter in enumerate(greeting):
    print(f"index :{index}, letter :{latter}")
"""

# ---zip metodu---
#iki farklı listeyi birleştirmek için kullanılır
# aynı indexte olanlar birleşir
# birden fazla eleman birleşebilir
# AYNI UZUNLUKTA olmaları gerekir

list1 = [1,2,3,4,5]
list2 = ["a", "b", "c" , "d", "e"]
list3 = [100,200,300,400,500]

print(list(zip(list1, list2, list3)))

for item in zip(list1, list2, list3):
    print(item)

for a, b, c in zip(list1, list2, list3):
    print(a, b, c)