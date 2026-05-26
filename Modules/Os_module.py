# işletim sistemi ile alakalı bilgiler sunar
# işletim sistemi hakkında ve klasörler hakında bilgi alabilriniz
# klasör ismi oluştuerablirrsibniz, klasör ismini değiştirebilirsiniz yada dosyalara birşeyler yapablirisinz

import os


result = dir(os)

result = os.name # bilgisayarın işletim sistemini söyler ( çıktı: nt)

result = os.getcwd() # hangi klasörde - hangi dizinde olduğunu söyler
#( bir path çıktısı verir: C:\Users\Neyca\Desktop\yazılım\Python\Modules)

#DOSYALARR

# os.mkdir("new_directory") #bu komut dosyanın olduğu ortama yeni klasör açar
# eğer belli bir yere klasör oluştrmak istiyorsan os.chdir komutu ile o klasöre git 
# eğer klasör varsa hata verrrir

# os.chdir("C:\\") # belirtilen dizine gider
# os.chdir("..") # bir üst klasöre geçer
# os.chdir("..\\..") # iki üst klasöre geçer 

# os.rename("new_directory", "Azerbaycandan-Salam") #dosyanın ismini değiştirir
#ilk eski adı diğeri yeni adı

# os.rmdir("yazılım") # eğer klasörün içi boşsa çalışır

# os.removedirs("Azerbaycandan-Salam\\yeniklasör")


result = os.getcwd()

# os.makedirs("C:\\Users\\Neyca\\Desktop\\yeniklasör") #klasörler oluşturur veya belli bir klasörün içine klasör oluşturur
# os.makedirs("new_directory\\yeniklasör")

print(result)


# LİSTEMEE

result = os.listdir() #dizin içerisinde olan dosylar ve kalsörleri gmsteriyor
# result = os.listdir("C:\\") # istediğin dizinin içindekileri alabilirsin

# filtreleme
for dosya in os.listdir():# bütün dosyaları tek tek inceleer
    if(dosya.endswith(".py")): # sadece .py uzantılı dosyaları sıralar
        print(dosya)


import datetime

dosya_bilgi = os.stat("Datetime_module.py")
# dosya hakında baya bir bilgi veriyor (ben sevdim wow diyorum)
# çıktı (saniye cinsinden):st_mode=33206, st_ino=4222124650757353,
# st_dev=1782881704, st_nlink=1, st_uid=0, st_gid=0, st_size=2186,
# st_atime=1779810712, st_mtime=1779808971, st_ctime=1779806650)

# ctime: dosyanın oluşturulma tarihi
# atime: dosyanın son erişilme tarihi
# mtime: dosyanın değiştirilme tarihi

result = dosya_bilgi.st_size/1024 # kaç kb olduğunu bulmak için



result = datetime.datetime.fromtimestamp(dosya_bilgi.st_ctime)
# bu komut dosyanın oluşturulma tarihini veriyor

result = datetime.datetime.fromtimestamp(dosya_bilgi.st_atime)
result = datetime.datetime.fromtimestamp(dosya_bilgi.st_mtime)

# istediğin programı çalıştırma
# os.system("notepad.exe") # eğer istediğin bir program çalıştırmak 
# istiyorsan onun pathini yazman gerek ama eğer klasörlerden birinde 
# veya dosyada boşluk varda dosyayı bulamıyor


#PATHHH YOL DİZİN PATHHH

result = os.path.abspath("Os_module.py") # konumunu dödürür
result = os.path.dirname(r"C:\Users\Neyca\Desktop\yazılım\Python\Modules\Os_module.py") #dosyanın tam yolu path

result = os.path.dirname(os.path.abspath("Os_module.py")) #beğendim
# eğer dosyanın tam yolunu bilmiyorsan bu komut
# sana dosyanın pathini (dizinini) verir

result = os.path.exists("Os_module.py") # o anki dizinde yazılı olan dosya varmı yokmu ona bakar 
# yazarsan istediğin dizinde dosyanın var olup olmadığınıda kontrol edebilirsin


result = os.path.isdir(r"C:\Users\Neyca\Desktop\yazılım\Python\Modules\Os_module.py") 
# verilen path bir dosyamı yoksa klasörmu olduğuna bakar, klasör => true : dosya => false

result = os.path.isfile(r"C:\Users\Neyca\Desktop\yazılım\Python\Modules\Os_module.py")
# verilen path bir dosyamı yoksa klasörmu olduğuna bakar, klasör => fasle : dosya => true

result = os.path.join("C:\\", "deneme", "deneme1", "deneme2") # istediğimiz pathi oluşturabiliyoruz (işe yarar)

result = os.path.split( r"C:\Users\Neyca\Desktop\yazılım\Python\Modules\Os_module.py,")
# çıktı: ('C:\\Users\\Neyca\\Desktop\\yazılım\\Python\\Modules', 'Os_module.py,')

result = os.path.splitext("Os_module.py")
# çıktı: ('Os_module', '.py') uzantısı dosya isimiden ayırır

print(result[0])