# ******YÖNTEM 1******

# import math

# Math_module modülünün içine math modülünü ekliyor

# value = dir(math) # içindeki bütün komutları diziye kaydeder
# value = help(math) # içindeki komutların nasıl çalışacağı anlatır
# value = help(math.factorial) # belirli bir komutun nasıl çalışacağı anlatır

# value = math.sqrt(49) # karekök alır
# value = math.factorial(5) #faktöriyelini alır
# value = math.floor(5.9) # sayıyı ağagı yuvarlar
# value = math.ceil(5.9) #sayıyı yukarı yuvarlar

# print(value)


# import math as islem
# # math kullanmak yerine istediğimiz ismi verebiliyoruzz

# value = islem.sqrt(49)
# value = islem.factorial(5)

# print(value)


# from math import *
# # bu şekilde modüle bir isim vermeden 
# # direk olarak kullanabiliyoruaz
# # ve modüldeki HER ŞEYİ koda ekliyoruz

# value = factorial(5)
# value = sqrt(49)


# print(value)


from math import factorial,sqrt

value = factorial(5)
value = sqrt(49)

print(value)