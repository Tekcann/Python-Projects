# BANKAMATİK UYGILAMASI

# bir sözlük oluşturduk
Ahmet_account = {
    "name" : "Ahmet",
    "account_no" : "123456",
    "balance" : 3000,
    "overdraft_account" : 2000
}

Suleyman_account = {
    "name" : "Süleyman",
    "account_no" : "121314",
    "balance" : 12000,
    "overdraft_account" : 5000
}

# kişinin adını ve hesapno sunu isteyelim eğer 
# bilgileri doğru ise hesabına ulaşabilsin. yanlışsa 3 deneme hakkında sonra hesap bloke olsun
# hesabında ne yapmak istediğini soralım
# iki seçenek ya para yatırsın yada para çeksin
# eğer para çekerken bakiyesi yetersiz kalırse ek hesap kullanılsınmı diye sorsun 
# ve eğer isterse ek hesap ve bakiyesinin etip yetmediğini kontrol edelim ve
# yeterse parayı verelim yetmezse parayı çekemezsini diyelim toplam bakiyeyi yazdıralım 
def kelimeDuzelt(kelime):
    kelime = kelime.strip(' ')
    kelime = kelime.lower()
    kelime = kelime.replace(" ", "")
    return kelime

def paraCek(hesap, miktar):
    
    print(f"Hesabınızda :{hesap["balance"]} Tl para bulunmaktdır.")
    print(f"Ek hesabınızda ise {hesap["overdraft_account"]} tl bulunmaktadır.")
    print(f"Harcanacak tutar :{miktar} tl")
    is_ok = input("işlem onayı için (E/H) :")
    is_ok = kelimeDuzelt(is_ok)
    if(is_ok == "e"):
        if (hesap["balance"] >= miktar):
            print("Paranızı alabilirsiniz")
            hesap["balance"] -= miktar
        else:
            toplam = hesap["balance"] + hesap["overdraft_account"]

            if (toplam >= miktar):
                ekHesapKullanimi = input("Ek Hesap kullanılısın mı (E/H)")
                ekHesapKullanimi = kelimeDuzelt(ekHesapKullanimi)

                if(ekHesapKullanimi == "e"):
                    print("paranızı alabilirisiniz")
                    hesap["balance"] = 0
                    toplam -= miktar
                    hesap["overdraft_account"] = toplam
                else:
                    print(f"{hesap["account_no"]} nolu hesapınızda {hesap["balance"]} bakiye bulunmaktadır.")
            else:
                print("Bakiyeniz Yetersiz")
    else:
        print("İşlem yapılamayacak")   

def paraEkle(hesap, miktar):
    print(f"{hesap["account_no"]} lu hesapınıza {miktar} para eklenecektir")
    is_ok = input("Onaylıyor musunuz (E/H)")
    is_ok = kelimeDuzelt(is_ok)
    if(is_ok == "e"):
        hesap["balance"] += miktar
        print(f"Hesabınıza :{miktar} tl para eklendi")
        print(f"yeni bakiyeniz {hesap["balance"]}")
    else:
        print("işlem iptal edildi")


def kisiKontrol(name, account_no):
    global user
    if(name == Ahmet_account["name"]) and (account_no == Ahmet_account["account_no"]):
        user = Ahmet_account["name"]
        print(f"{Ahmet_account["name"]} Bey hoş geldiniz")
        print("*" * 50) 
        is_correct = True
    elif(name == Suleyman_account["name"]) and (account_no == Suleyman_account["account_no"]):
        user = Suleyman_account["name"]
        print(f"{Suleyman_account["name"]} Bey hoş geldiniz")
        print("*" * 50)  
        is_correct = True
    else:
        print(f"Yanlış şifre veya isim girdiniz.")
        is_correct = False
    return is_correct, user
    

user_name = input("İsminizi Giriniz :")
user_name = user_name.capitalize()
user_no = input("Hesap no giriniz :")

is_correct,user = kisiKontrol(user_name, user_no)
while (True):
    if(is_correct == True):
        process = input("hangi işlemi yapmak istersiniz :\n(Para Çek)\n(Para Ekle)\n")
        process = kelimeDuzelt(process)
        if(process == "paraçek"):
            money = int(input("Kaç para Çekmek istersiniz :"))
            if(user == "Ahmet"):
                paraCek(Ahmet_account, money)
            elif(user == "Süleyman"):
                paraCek(Suleyman_account, money)
        elif(process == "paraekle"):
            money = int(input("Kaç para eklemek istersiniz :"))
            if(user == "Ahmet"):
                paraEkle(Ahmet_account, money)
            elif(user == "Süleyman"):
                paraEkle(Suleyman_account, money)
        print("*" * 50)
        conti = input("İşlemlere devam edilsin mi (E/H)")
        conti = kelimeDuzelt(conti)
        if(conti == "e"):
            continue
        else:
            exit()
            break




