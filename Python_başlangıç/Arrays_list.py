#*****DİZİLEEERRRRRRRR*****
"""
my_list = [1,2,3]
#birbirinden farklı veri tipleri tek dizide olabilir
my_list = ["bir",2 ,True ,5.6]
print(my_list)
"""

"""
list1 = ["one", "two", "there"]
list2 = ["four", "five", "six"]
numbers = list1 + list2
print(numbers)
print(len(numbers))#dizinin içiDEKİ elemanların sayısına ulaşılır
print(numbers[3])
"""
"""
userA = ["Ahmet", 18]
userB = ["Şahin", 21]
users = [userA , userB]
print(userA)
print(userB)
print(users[0][1])# iki boyutu bizelerin kullanımı
"""

#*****UYGULAMAAAAAA*****
"""
# birinic soru
arabalar =["BMW", "Mersedes", "Opel", "Mazda"]

# ikinci soru
print(len(arabalar))

#üçüncü soru
print(arabalar[0],arabalar[3])

#dördüncü soru
arabalar[3] = "Toyato"
print(arabalar)

#beşinci soru
print("Mersedes" in arabalar)

#altıncı soru
print(arabalar[-2])

#yedinci soru
print(arabalar[0:3])

#sekizinci soru
arabalar[-2:] = ["Toyota", "Renault"]
print(arabalar)

#dokuzuncu soru
daha_arabalar = arabalar + ["Audi", "Nissan"]
print(daha_arabalar)

#onuncu soru
del arabalar[-2]
print(arabalar)

#onbirinci soru 
print(arabalar[::-1])

#onikincisoru
studentA = ["Yiğit", "Bilgi", 2010, [70,60,70]]
studentB = ["Sena", "Turan", 1998, [80,80,80]]
studentC = ["Ahmet", "Tekcan", 2009, [80,90,100]]

print(studentA[0][::])
print(studentB[2])
print(studentC[3][0])

#13
resultA = (studentA[3][0] + studentA[3][1] + studentA[3][2])/3
print(f"{studentA[0]} {studentA[1]}, {2026 -studentA[2]} yaşındandır ve ortalaması {resultA}")
"""


#*****DİZİ METOTLARIIII*****
"""
numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ["a", "g", "s", "b", "y", "a", "s"]

val = min(numbers)#dizideki en küçük değeri bulur
val = max(numbers)#dizideki en BÜYÜk değeri bulur

val = min(letters)#alfabedeki sırasına göre seçer
val = max(letters)

# dizinin bir endeksinden başlar ve başka bir indeksine kadar devam eder
val =numbers[2:6]
val =numbers[::]

#var olan bir indexteki değer değiştirilebilir
numbers[4] = 40


#diziye yeni eleman ekleme işlemi
numbers.append(49)
#yada
#belli bir index e eleman eklemek isterse
numbers.insert(3, 78)

#diziden eleman SİLMEK istesek
numbers.pop() # en sonu siler yada index ver

#belli bir elemanı SİLMEK istersek
numbers.remove(10)

#elemanlar sıralamak
val = numbers.sort()#küçükten büyüğe sıralr
#ancak sıraladıktan sonra ters çevrilebilir
val = numbers.reverse()

#eleman sayısı
print(len(numbers))

#elemandan kaç tane var
print(numbers.count(10))

#herşeyi silemek
#numbers.clear()


print(numbers)
print(val)
"""

#*****UYGULAMAAAAAAAAAA*****
"""
names = ["Ali", "Yağmur", "Hakan", "Deniz"]
years = [1998, 2000, 1998, 1987]
#1. soru
names.append("Cenk")
print(names)

#2. soru
names.insert(0,"Sena")
print(names)

#3. soru
#names.remove("Deniz")
print(names)

#4. soru
a = "Ali" in names#true yada false değer verir
print(a)

#5. soru
print(names[4])

#6. soru
names.reverse()
print(names)

#7. soru
names.sort()
print(names)

#8. soru
years.sort()
print(years)

#9. soru
str = "Chevrolet, Daica"
print(str.split(","))

#10. soru
min = min(years)
max = max(years)
print(min , max)

#11. soru
print(years.count(1998))

#12. soru
years.clear()
print(years)

#13. soru
markalar = []
markalar.append(input("birinci marka :"))
markalar.append(input("ikinci marka :"))
markalar.append(input("üçüncü marka :"))

print(markalar)
"""
