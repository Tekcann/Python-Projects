# fonksiyondan önce veya fonksiyondan saonra 
# bell işlemlerin yapılmasını istediğimiz zaman bu komutları kullnaılır
# birden fazla fonksitonda aynı işlemleri uygulayacaksak 
# tek fonksiyonu decorator olarak kullanmak kodu daah modüler yapar


def my_decorator(func):# bu bir fonksiyon (funch)
    def wrapper(name):
        print("fonksiyondan önceki işlemler")
        func(name)
        print("fonksiyondan sonraki işlemler")
    return wrapper

@my_decorator # fonkiyonu gönderir
def sayHello(name):
    return print("hello " + name)

def sayGreeting():
    print("greeting")

# sayHello = my_decorator(sayHello)
# bu kod satırı ile @my_decorator aynı işlemi yapar

sayHello("Ali")



import math
import time


def calculate_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        time.sleep(1)

        func(*args, **kwargs)

        finish = time.time()
        print("fonksiyon " + str(finish - start) + " saniye sürdü")
    return inner

@calculate_time
def usAlma(a, b):
    print(math.pow(a,b))

    
@calculate_time
def faktoriyel(num):
    print(math.factorial(num))

@calculate_time
def toplama(a,b):
    print(a+b)





usAlma(2,3)
faktoriyel(4)
toplama(10, 20)