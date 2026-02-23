x = 10

# # kendi hatamızı oluşturduk
# if( x> 5):
#     raise Exception("x % ten büyük değer alamaz")

def check_passwod(psw):
    import re # kontrol işlemlerini haypmak için
    if(len(psw) < 8):
        raise Exception("Paralo en az 8 karakter olmalıdır")
    
    elif not(re.search("[a-z]", psw)):
        raise Exception("Paralo küçük harf içermelidir")
    
    elif not(re.search("[A-Z]", psw)):
        raise Exception("Paralo büyük harf içermelidir")
    
    elif not(re.search("[_@$]", psw)):
        raise Exception("Parola alpha numaric karakte içermeldir")
    elif(re.search("\\s", psw)):
        raise Exception("Parolada boşuk içeremez")
    
password = "1aA4_678"

try:
    check_passwod(password)
except Exception as e:
    print(e)
else:
    print("geçerli Parola")
finally:
    print("kontrol Tamamlandı")


class Person:
    def __init__(self, name):
        if(len(name) > 10):
            raise Exception("name alanında fazla karakter bulunuyor")
        else:
            self.name = name
        
try:
    p = Person("Ahmet")
except Exception as e:
    print(e)
    