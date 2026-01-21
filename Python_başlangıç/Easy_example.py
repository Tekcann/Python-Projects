"""
custemer_name = "Ahmet"
custemer_surname = "Tekcan"
custumer_fullname =custemer_name +' '+ custemer_surname
custumer_gender = True #erkekse true olsun
custumer_id = "123123"
custumer_birthday = "17.07.2009"
custumer_address = "Adana mersin yersin"
custumer_age = "17"

print(110+ 1100.5 + 356.95)
"""

#yeni konu veri dönüşümleri
"""
x =input("1.sayı : ")
y =input("2.sayi: ")
toplam = int(x) + int(y)

print(toplam)
"""

#dönüşümler
"""
pi = 3.14

print("Dairanin alanı ve  çeversini hessaplama")
yari_cap = input("yarı çap :")
yari_cap = float(yari_cap)
dairenin_alani = pi * yari_cap **2
print("Dairenin Alanı: "+ str(dairenin_alani))

dairenin_cevresi = 2* pi * yari_cap
print("Dairenin Çevresi :" + str(dairenin_cevresi ))
"""

# name = "Sadık"
# surname = "Turan"
# age =36
"""
greeting ="My name is "+ name + " "+surname + "and\nI am "+ str(age) + " yet"
lenght = len(greeting) -1
print(greeting)
print(name[0])
print(greeting[len(greeting) -1]) #yada
print(greeting[lenght])

print(greeting[3:7])
istenilen indexten başlayıp istenilen indexe kadar alır
ikinci parametreyi yazmazsan kelime bitene kadarki kısmı alır
birinci parametreyi yazmassan sıfırıncı indexten başlar istenilen yere kadar alır

website= "https:/www.deneme.com"
course = "Python Kursu: Baştan sona programlama (40 saat)"
# birinci soru
lenght = len(course)
print(lenght)
"""
"""
#ikinci soru
www = print(website[7:10])

#üçüncü soru
com = print(website[18:21])

#dördüncü soru 
ilk15 = print(course[:15])
son15 = print(course[32:47])

#beşinci soru
print(course[::-1])

name, surname, age, job = ("Bora", "Yılmaz", 32, "Mühendis")

#altıcı soru
print(f"Benim adım {name} {surname}\nBen {age} yaşındayım\nMesleğim {job}")

#yedinci soru 
s = "Hello world"
print(s.replace('w', 'W'))


#sekizinci soru
print("abc" * 3)
"""