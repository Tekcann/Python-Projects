import random
class User:
    def __init__(self, name, password, balance = 0, overdraftAccount = 0):
        self.name = name
        self.password = password
        self.balance = balance
        self.overdraftAccount = overdraftAccount
        self.ID = random.randint(0,100)

        self.ID = {
            "name" : self.name,
            "password" : self.password,
            "balance" : self.balance,
            "overdraftAccount" : self.overdraftAccount
        }
    def mainMenu(self):
        print("ATM YE HOŞGELDİNİZ".center(30,"*"))

        mainprocess = input("Hesabınız Var mı (E/H)")

        if(mainprocess == "E"):
            name = input("Adınızı Giriniz: ")
            password = input("Şifrenizi Giriniz: ")
            self.check(name, password)
        else:
            print("O ZAMAN YENİ HESAP AÇIN".center(27, "*"))
            self.newAccount()

    def newAccount(self):
        name = input("İzminizi girin: ")
        password = input("Şifrenizi belirleyin: ")
        print("Hesabını oluşturulmuştur.".center(35, "*"))

        self = User(name, password)
        self.mainMenu()


    def check(self, name, password):
        
        if(self.name == name):
            if(self.password == password):
                self.information()
            else:
                print("şifrenizi Yanlış Girdiniz")
                self.mainMenu()
        else:
            print("İsminizi Yanlış Girdiniz")
            self.mainMenu()
            



    def information(self):
        print("*"*50)
        print(f"Hoşgeldiniz {self.name}" + 
              f"\nHesabınızda: {self.balance} TL bulunmaktadır." +
              f"\nEk hesabınızda: {self.overdraftAccount} TL bulunmaktadır.")
        
        self.process()

    def process(self):

        print("*"*50)
        process = input("Yapmak istediğiniz işlem nedir?" +
                        "\nPara Çek" +
                        "\nPara Yükle" +
                        "\nHesaptan Çık" +
                        "\nİşlem: ")   
        
        if (process == "Para Çek"):
            self.cashWithdrawal()
        elif(process == "Para Yükle"):
            self.addMoney()
        elif(process == "Hesaptan Çık"):
            self.mainMenu()
        else:
            print("Yanlış giriş yaptınız.")
            self.process()

    def cashWithdrawal(self):
        amount = int(input("Kaç para çekmek istersiniz: "))        
        is_ok = input(f"{amount} TL para çekme işlemini onaylıyor musunuz? (E/H)")
        if (is_ok == "E"):
            if(self.balance >= amount):
                self.balance -= amount
                print("Paranızı alabilirsiniz")
            else:
                total = self.balance + self.overdraftAccount
                use_overdraftAccount = input("Ek habınız kullanılsın mı? (E/H)")

                if(total >= amount) and (use_overdraftAccount == "E"):
                    total -= amount
                    self.balance = 0
                    self.overdraftAccount = total
                
                else:
                    print("Bakiye Yetersiz")

        else:
            print("İşlem yapılmayacak")

        print("*" * 42)
        self.information()
    
    def addMoney(self):
        amount = int(input("Kaç para yatırmak istersiniz: "))
        is_ok = input("Onaylıyor musunuz? (E/H)")

        if(is_ok == "E"):
            self.balance += amount
            print(f"Hesabınıza {amount} TL para yatırılmıştır" +
                  f"\nYeni bakiyeniz: {self.balance}")
        else:
            print("İşlem Yapılmayacak")
        
        self.information()




user = User("Ahmet", "123456", 3500, 2000 )
user.mainMenu()
    
        