message = "Hello There. My name is Şahin Tekcan"

#*********String Metotlar*********
"""
# BÜTÜN KARAKTERLERİ BÜYÜK HARFLE YAZAR
message = message.upper()

# bütün karakterleri küçük harfle yazar
message = message.lower()

# Her Kelimenin Baş Harfi Büyük Olsun İstersek
message = message.title()

# Verilen ifadenin sadece ilk harfini büyük yazar
message = message.capitalize()

#başta ve sonda bulunan boşluk karakterlerini siler
#not: strip komutunun içine silmek istediğiniz harfleri yazarsanız siler
message = message.strip()
message = message.strip("hlo")

# Her, bir, kelimeyi, boşluk, yerlerinden, ayırır, 
message =message.split()
# Eğer istersek ayırmasını istediğimiz bölümleri yazabiliriz
#message =message.split('.')

#BirbirindenAyrıKelimelerBirleştirmekİçinKullanılır
message =' '.join(message)

#Cümle icerinde bir kelimenin var olup olmadığını kontrol eder
index = message.find('Hello')
print(index)#metne değişiklik yaparsan onagöre yazar

#kelimanin hangi harfle bitiğini ve başladığını sorgulamak için
is_found = message.startswith("H")
is_found = message.endswith("n")


#Cümle içerisinde bir arama yapar ikinci parametreyi o kelimenin yerine yazar
message =message.replace("Tekcan", "Deneme").replace(" ", "*")

#kelmeyi daya büyük bir boşluğun ortasına yerleştirir
#kelimeyi ortalar 
message =message.center(50,"*")

print(message)
"""


#*****UYGULAMAAAAAAAA*****
website= "https:/www.deneme.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

#birinci soru
Hello_World ="  Hello World  "
print(Hello_World.strip())

#ikinci soru                     
index = website.find("deneme")
print(index)
print(website[11:17])

#yada
print(website.strip("htps:/w.com"))



#üçüncü soru
print(course.lower())

#dördüncü soru
print(website.count("e"))

#beşinci soru
print(website.startswith("www"))
print(website.endswith("com"))

#altıncı soru
print(website.count(".com"))

#yedinci soru
print(course.isalpha())#sadece harfler varsa true döner
print(course.isdigit())#gelen değer sayısal ifademi

#sekizinci soru
print("Contents".center(50,"*"))

#dokucuncu soru
print(course.replace(" ","-"))

#onnuncu soru
print("Hello World".replace("World","There"))

#onbirinci soru
print(course.split(" "))