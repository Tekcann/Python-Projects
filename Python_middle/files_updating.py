path = r"C:\Users\Neyca\Desktop\mesleki raporlar ve proje dosyaları\yazılım\Python\My_Coding_Files\deneme.txt"



#          r+ hem okuyup hem yazmak için
# dosyanın en başından başlayarak olan metnin üzerine yazdırıyor
with open(path, "r+", encoding="utf8") as file:
    file.seek(20)
    file.write("11Yazılımsal")


with open(path, "r+", encoding="utf8") as file:
    print(file.read())   


# ******SAYFA SONUNDA GÜNCELLEME******

#          a ile dosyayı açarsak dosyanın en sonuna ekler
with open(path, "a", encoding="utf8") as file:
    file.write("11Yazılımsal")

with open(path, "r+", encoding="utf8") as file:
    print(file.read()) 
    # dosyayı okumak stediğimiz içi her seferinde okuma modunda modunda açmamız gerekiyor


# ******SAYFA BAŞINDA GÜNCELLEME******

with open(path, "r+", encoding="utf8") as file:
    content = file.read() 
    content = "12Denemesel\n" + content 
    file.seek(0)
    file.write(content)
    print(content)

with open(path, "r", encoding="utf8") as file:
    print(file.read()) 


# ******SAYFA ORTASINDA GÜNCELLEME******

with open(path, "r+", encoding="utf8") as file:
    liste = file.readlines()
    liste.insert(len(liste), "14Bilgisayar\n")
    file.seek(0)
    # for i in liste:
    #     file.write(i)

    # YA DA ***

    file.writelines(liste)
    
with open(path, "r", encoding="utf8") as file:
    print(file.read())