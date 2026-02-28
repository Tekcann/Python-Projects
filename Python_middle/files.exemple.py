ogrenci_verileri = r"C:\Users\Neyca\Desktop\mesleki raporlar ve proje dosyaları\yazılım\Python\My_Coding_Files\sinav_notlari.txt"
ogrenci_sonuclari = r"C:\Users\Neyca\Desktop\mesleki raporlar ve proje dosyaları\yazılım\Python\My_Coding_Files\sonuclar.txt"
# Not uygulaması

def notHesapla(satir):
    satir = satir[:-1]
    liste = satir.split(":")
    ogrenciAdi = liste[0]
    ogrenciNotlari = liste[1].split(",")

    not1 = int(ogrenciNotlari[0])
    not2 = int(ogrenciNotlari[1])
    not3 = int(ogrenciNotlari[2])
    ort = (not1+not2+not3) / 3

    if(ort >= 90) and (ort <= 100):
        harf = "AA"
    elif(ort >=85) and (ort <= 89):
        harf = "BA"
    elif(ort >=65):
        harf = "CC"
    else:
        harf = "FF" 


    return ogrenciAdi + " " + harf + "\n"   

def notOku():
    with open(ogrenci_verileri, "r", encoding="utf8") as file:
        for satir in file:
            print(notHesapla(satir))



def notGir():
    ad = input("öğrenci adı: ")
    soyad = input("öğrenci soyadı: ")
    not1 = input("birinci not: ")
    not2 = input("ikinci not: ")
    not3 = input("üçüncü not: ")

    # her öğrencinin bilgilerini sırasıyla ekliyoruz
    with open(ogrenci_verileri, "a", encoding="utf8") as file:
        file.write(f"{ad} {soyad}:{not1},{not2},{not3}\n")
        # : ve , ler bizim için ayrım noktalaarı



def kayıtEt():
    with open(ogrenci_verileri, "r", encoding="utf8") as file:
        liste = []

        for i in file:
            liste.append(notHesapla(i))

    with open(ogrenci_sonuclari, "w", encoding="utf8") as file2:
        for i in liste:
            file2.write(i)

        


while True:
    islem = input("1-Notları Oku\n2-Not Gir\n3-Kayıt Et\n4-Çıkış Yap\n")

    if(islem == "1"):
        notOku()
    elif(islem == "2"):
        notGir()
    elif(islem == "3"):
        kayıtEt()
    else:
        break

