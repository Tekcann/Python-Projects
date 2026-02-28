# dosya okuma komutları
path = r"C:\Users\Neyca\Desktop\mesleki raporlar ve proje dosyaları\yazılım\Python\My_Coding_Files\deneme.txt"

#             ******with******
# with komutu ile dosya açtığımız zaman altına 
# kod bloğu oluşturabiliyoruz bu sayede kod bloğu 
# bitince dosyada kendiliğinden kapannıyor
with open(path, "r", encoding="utf-8") as file:
# böyle kullanılıyor işte anlarsın
    content = file.read()
    print(content)
    file.seek(50) #imleci istediğimiz sıraya koymamızı sağlıyor
    print(file.tell()) #imlecin konumunu gösterir
    content2 = file.read()
    print(content2)

