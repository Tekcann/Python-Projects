#tarih ve zamanla ilgili işlemler için
# **import datetime**
# bu şekilde bütün klaslar gelir


# from datetime import date
# from datetime impot time
from datetime import datetime
from datetime import timedelta
# sadece datetime sınıfını projeye ekler


simdi = datetime.now() # anlık saat bilgisi ham hali

result = simdi.year
result = simdi.month
result = simdi.day
result = simdi.hour
result = simdi.minute
result = simdi.second


result = datetime.ctime(simdi) # tarihi daha anlaşılır bicimde gösteririr

result = datetime.strftime(simdi, '%Y') # sadece yıl
result = datetime.strftime(simdi, '%X') # sadece saat
result = datetime.strftime(simdi, '%d') #sadece gün
result = datetime.strftime(simdi, '%A') # sadece gün ama string
result = datetime.strftime(simdi, '%B') # sadece ay ama string
result = datetime.strftime(simdi, '%D') # ay, gün, yıl şeklide 
result = datetime.strftime(simdi, '%Y %B %A') 

# harflerin anlamları ve diğer şeyler için
# w3school.com python datetime modül internette arat


print(result)


t = "21 Nisan 2010"
gun, ay, yil = t.split()

print(gun)
print(ay)
print(yil)

t = "15 April 2019 hour 10:12:30"
dt = datetime.strptime(t, "%d %B %Y hour %H:%M:%S")

print(dt) #çktısı 2019-04-15 10:12:30

print(dt.year) # çıktıaı 2019


birthday = datetime(1999, 5, 9, 12, 30, 15)

print(birthday) #çıktıı 1686-05-09 00:00:00 ve ya 1686-05-09 12:30:15
#boş kalan kısım 0 kabul ediliyor

result = datetime.timestamp(birthday) # saniy bilgisi 926242215.0 ( ne işe yarar bilmiyorum)
result = datetime.fromtimestamp(result) # tekrardan normal tarihe dönüştürür 1999-05-09 12:30:15

result = datetime.fromtimestamp(0) # 1970-01-01 03:00:00 bilgisayarların milad tarihi 


tdelta = simdi - birthday # timedelta objesi  (çıkıt 9879 days, 5:46:42.369623)

tdelta = tdelta.days # sadece gün bilgisi döndürür 9879


print(tdelta)

print(simdi)
result = simdi + timedelta(days=10) # güne on ekler eğer takvime göre gerekirse ayı 1 arttır
#topla çıkar çarp bül ya da gün ay yıl takıl kafana göre ötele flana yani
print(result)



