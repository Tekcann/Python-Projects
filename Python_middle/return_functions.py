def usAlma(number):
    

    def inner(power):
         return number ** power

    return inner

# inner fonkisyonu artık two oluyor
two = usAlma(2)
print(two(3))


three = usAlma(3) #bu ana fonksiyon "usAlma"
print(three(4)) #bu da alt fonksiyonu "inner"



def yetki_sorgula(page):
    def inner(role):
        if(role == "Admin"):
            return "{0} rolü {1} sayfasına ulaşabilir".format(role, page)
        else:
            return "{0} rolü {1} sayfasına ULAŞAMAZ".format(role, page)
    return inner   

user1 = yetki_sorgula("Product Edit") #yetki sorgula fonkiyonu burada çalışıyor
print(user1("User")) # inner fonksiyonu burada çalışıyor



def islem(islem_adi):
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam
    
    def carpma(*args):
        carpım = 1
        for i in args:
            carpım *= i
        return carpım
    
    if (islem_adi == "Toplama"):
        return toplam
    else:
        return carpma
    
toplama = islem("Toplama")
print(toplama(2,3,5,48,6))

carpma = islem("Çarpma")
print(carpma(2,2,2,2,2,2))