# key - value

#41 => kocaeil  34 => istanbul
# örnek başlangıç


#         SÖZLÜK YAPISIIII

sehirler = ["kocaeli", "istanbul"]
plakalar = [41, 34]

print(plakalar[sehirler.index("kocaeli")])
print(plakalar[sehirler.index("istanbul")])
#mantığı kavramak için yazdık ////

#********KEY-VALUE MANTIĞIIIII********

#print(plakalar["kocaeli"]) => bu şekilde yazdığımızda bizi 41 e götürecek

#değişkenAdı = {"key": "value"} //bu şeklide

plakalar = {"kocaeli" : 41, "istanbul" : 34}

print(plakalar["kocaeli"])
print(plakalar["istanbul"])

#eğer yeni eleman eklemek istersek
plakalar["ankara"] = 6 #bu kadar

#değer değiştirmek istersek
plakalar["kocaeli"] = "new value"

print(plakalar)


#OYEEEEE

users = {
    "SadıkTuran" : {
        "age" : 36,
        "roles" : "user",
        "email" : "deneme.com",
        "adres" : "kocaeli",
        "tel" : "123456789",
        
    },
    "CınarTuran" : {
        "age" : "2",
        "roles" : ["admin", "user"],
        "email" : "2deneme2.com",
        "adres" : "kocaeli",
        "tel" : "123123123"
    }
}
#ilk parametra birinci key ikinci parametra ikinci key 
#istediğimiz seçmek için diziler mandığı işliyor
print(users["CınarTuran"]["roles"][0])

#******UYGULSAAAAA********

ogranciler = {}

numara = input("öğrenci numarası :")
ad = input("öğrenci adı :")
soyad = input("ögrenci soyadı :")
tel = input("öğrenci telefon numarası :")

ogranciler[numara] = {
    "ad" : ad,
    "soyad" : soyad,
    "tel" : tel
}
print("işlem başarıyla gerçekleştirildi")
print("yeni kayıt işlemlerine başla")

numara = input("öğrenci numarası :")
ad = input("öğrenci adı :")
soyad = input("ögrenci soyadı :")
tel = input("öğrenci telefon numarası :")

ogranciler[numara] = {
    "ad" : ad,
    "soyad" : soyad,
    "tel" : tel
}
print("işlem başarıyla gerçekleştirildi")
print("yeni kayıt işlemlerine başla")

numara = input("öğrenci numarası :")
ad = input("öğrenci adı :")
soyad = input("ögrenci soyadı :")
tel = input("öğrenci telefon numarası :")

ogranciler[numara] = {
    "ad" : ad,
    "soyad" : soyad,
    "tel" : tel
}
print("işlem başarıyla gerçekleştirildi")

print(ogranciler)

print("*"*50)
#bir input değeri değişkene atıyoruz
girilen_numara = input("istediğiniz numarayı giriniz :")
#girilen değere karşılık gelen elemanı ve diziyi komple 
#ogrenci değişkenine kaydediyoruz.(işimizi kolaylaşırıyoe)
ogrenci = ogranciler[girilen_numara]


print(f"{girilen_numara} lı öğrencinin ismi {ogrenci["ad"]} {ogrenci["soyad"]} ve telefon numarası {ogrenci["tel"]} dirr.")
print(ogrenci)


# SÖZLÜKKKKKKKKKK falan filan


