# value veri tipi değişkenler 
#string, int, floa, bool, falan filan

#burada değişkenin değeri ile ilgilenilir
"""
x = 5
y = 25

x = y
# burada yapılan değişkenin değişikleri 
# sadece o değişkeni etkiler
y = 10
print(x,y)
"""
#Reference veri tipi - Reference Data Type

#burada deşikenin saklandığı adres ile işlem yapılıe


a = ["apple", "banana"]
b = ["apple", "banana"]

a = b # iki diziyi birbirine kenetleniyor 
#birinin değişikliyi diğerininde de görülüyor

b[0] = "grape"
# sadece b dizisindeki eleman değişikliği yapılıyor
# ama iki dizideki elemanlar aynı şekide değişiyor
# garip
print(a,b)