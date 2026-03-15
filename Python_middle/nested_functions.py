# greeting içerisinde adres tutar veri değil
def greeting(name):
    print(f"hello {name}")

# print(greeting("Ahmet"))
# print(greeting)

sayHello = greeting

print(greeting("Ahmet"))
print(sayHello("Ahmet"))

del sayHello 
# adres üzerindeki bilgiyi SİLMEZ sadece değişkeni siler



# encapsulation =>
def outer(num1):
    print("outher")
    def inner_increment(num1):
        print("inner")
        return num1 + 1
    num2 = inner_increment(num1)
    print(num1)
    print(num2)
    
outer(10)
# inner_increment => alt fonksiyon olduğu için cağrılamaz


def factorial(number):
    if not(isinstance(number, int)):
        raise TypeError("number must be intager")
    if not(number >=0):
        raise ValueError("number must be zero or positive")
    def inner_factorial(number):
        if(number <= 1):
            return 1
        return number * inner_factorial(number - 1)
    return inner_factorial(number)


try:
    print(factorial(5))
except Exception as ex:
    print(ex)