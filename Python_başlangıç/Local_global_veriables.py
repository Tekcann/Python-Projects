# --------------------------------------------
# ********GLOBAL ve LOCAL  VARİABLES**********
# --------------------------------------------

# global scope
x = "global x"

def function():
    # local scope
    x = "local x"
    # eğer Fonkisyonun içerisinde x değişkeni yoksa
    # global olan değişkeni alır
    print(x)

function()
print(x)

# ********************
# global name
name = "Çınar"

def changeName(new_name):
    # local name
    name = new_name
    print(name)

changeName("Ahmet")
print(name)

#*********************

name = "global string"

def greeting():
    # name = "global string" ifadesi greeting fonksiyonunun globalidir

    name = "Ahmet" # yorum satırı yapıldığında
    # eğer değşkenin bir üstünde name değişkeni yoksa o zaman daha dış çerçeveye bakar
    def hello():

        # name = "Ahmet" ifadesi hello fonkisyonu için globaldir
        # iç içe fonksiyonlarda global olan
        # bir dış fonksiyondur
        
        print("Heloo "+ name)

    hello()

greeting()
print(name)


#********************************

# bu komut bloğunda x değişkeni lokal olduğu için yapılan
# değişiklikler sadee fonksiyonun içini etkiliyor

x = 50

def test(x):
    print(f"x : {x}")

    x = 100
    print(f"change x to {x}")

test(x)
print(x)


#***************************************

# burada ise x değişkenini globalden al dediğimiz için 
# x üzerinde yapılan değişiklikler sonrasında da devam ediyor 

x = 50

def test():
    # global olan x i kullan diyoruz
    global x
    print(f"x : {x}")
    
    x = 100
    print(f"change x to {x}")

test()
print(x)