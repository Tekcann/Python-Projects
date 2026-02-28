# Dosya açmak ve oluşturmak içi open() fonksiyonu kullanılır
# Kullanımı: open(dosya_adi, dosya_erişme_modu)

# dosya_erişme_modu => dosyayı hangi amaçla kullanacağımızı belirtir

# "w": (Write) yazma modu, Dosyayı konumda oluşturur
#       **Dosyayı konuma oluşturur
#       **Dosya içeriğini siler ve yeniden ekleme yapar

path = r"C:\Users\Neyca\Desktop\mesleki raporlar ve proje dosyaları\yazılım\Python\My_Coding_Files\deneme.txt"
path2 = r"C:\Users\Neyca\Desktop\mesleki raporlar ve proje dosyaları\yazılım\Python\My_Coding_Files\deneme2.txt"
# değer dosya ile kodun dosyayı aynı kasörde ise sadece isim yazsakta oluyor

file = open(path, "w")
file.close()

# Türkçe karakter tanınması için gerekli => encoding= "utf-8"
file = open(path, "w", encoding= "utf-8")
file.write("Ahmet Şahin Tekcan")
print(file)
file.close()

# "a": (Append) ekleme, Dosya konumda yoksa oluşturur

file = open(path, "a", encoding="utf-8")
file.write("Ahmet Tekcan\n")
file.close()


# "x": (Create) oluşturma, Dosya zaten varsa hata verir.

file = open(path2, "x", encoding="utf-8")


# "r": (Read) okuma, varsayılan Dosya konumda yoksa hata verir
 
try:
    file = open(path2, "r", encoding="utf-8")
except:
    print("dosya okuma hatası")
finally:
    print("Dosya kapandı")
    file.close()


file = open(path, "r", encoding="utf-8")

# for döngüsü ile veri okuma
for i in file:
    print(i, end="")

# İki işlemde aynı işlevi yapıyor aşağıdaki daha mantıklı

# read fonksiyonu ile veri okuma
content = file.read()

# print(content) # bütün içeriği okur ve imleç dosyanın en sonuna ulaşır

# Dosyanın ilk 5 karakterini alır
content = file.read(5)
print(content)


#     ******readline()******  
#eğer satırı komple okumak istiyorsak

print(file.readline())# satırı komple okur ve imleci aşağı indirir
print(file.readline())# bu sebeple dosyayı kapatmadan her okuma 
print(file.readline())# yaptığımızda alt satıra ulaşırız
print(file.readline(), end="")
print(file.readline(), end="")
# eğer dosyayın içerisindeki satır boşsa boş değer gönderir

#     ******readlines()****** 
liste = file.readlines()
print(liste)

file.close()

