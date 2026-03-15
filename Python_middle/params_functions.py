def toplama(a,b):
    return a+b
def cıkarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b

# Gönderdiğimiz parametra bir fonksiyon olduğu için 
# bu değişkenler bir veri yerine adres değerini kaydederler 
# bu sayede biz fonkisyonlara parametre olarak fonksiyon gönderbiliyoruz
# bu işe yarayabilir
def islem(f1,f2,f3,f4,islem_adi):
    if(islem_adi == "Toplama"):
        print(f1(2,3))
    elif( islem_adi == "Çıkarma"):
        print(f2(5,3))
    elif(islem_adi == "Çarpma"):
        print(f3(3,3))
    elif(islem_adi == "Bölme"):
        print(f4(8,2))
    else:
        print("Geçersiz işlem...")


islem(toplama,cıkarma,carpma,bolme,"Toplama")
islem(toplama,cıkarma,carpma,bolme,"Çıkarma")
islem(toplama,cıkarma,carpma,bolme,"Çarpma")
islem(toplama,cıkarma,carpma,bolme,"Bölme")
islem(toplama,cıkarma,carpma,bolme,"Sanane")