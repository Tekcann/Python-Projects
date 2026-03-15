def my_decorator(func):
    def wrapper():
        print("fonksiyondan önceki işlemler")
        func()
        print("fonksiyondan sonraki işlemler denem")
    return wrapper()

@my_decorator
def sayHello():
    return print("hello")

def sayGreeting():
    print("greeting")



