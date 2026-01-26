# *****class*****

class Person:

    # ***class attributes***
    # her zaman kullanılmayacak bir özellik için
    address = "no information"

    # ***constructor (yapıcı Metod)***

    # mutlaka gerekli olanlar bu şekilde
    # bu metot oluşturulan her bir obje için çalışır
    # bu yüzden yapıcı metod denir

    def __init__(self, name, year):
        # **object attributes**
        self.name = name
        self.year = year
        print(f"{name} için init metodu çalıştı")
        print("*"* 50)

    # **methods**

    # *instance methods* [ objelere hismet edecek metotlar]
    def intro(self):
        print("Hello There ")

    # *instance methods*
    def calculateAge(self):
        return 2026 - self.year
    

# ***object (instance)***

p1 = Person("Ahmet", 1990) # p1 obje oldu
p2 = Person(name = "Ada",year = 2008) # iki kullanımda doğru

# **updating*
p1.name = "Ali"
p2.address = "İzmir"

# **accesing object attributes**
print(f"name: {p1.name}, year: {p1.year}, adres: {p1.address}")
print(f"name: {p2.name}, year: {p2.year}, adres: {p2.address}")


ad = p1.name
print(p2)
print(ad)
print(type(p1))
print(type(p2))

p1.intro()
p2.intro()

print(f"adım: {p1.name} ve yaşım {p1.calculateAge()}")
print(f"adımÇ {p2.name} ve yaşım {p2.calculateAge()}")


class Circle:
    # Class object attribute
    pi = 3.14

    def __init__(self, yaricap = 1):
        self.yaricap = yaricap

    # Methods
    def cevre_hesapla(self):
        return 2 * self.pi * self.yaricap

    def alan_hesapla(self):
        return self.pi * (self.yaricap ** 2)  
    
c1 = Circle() # eğer yarıçap verilmezse 1 olarak kabul eder. çünkü ben öyle istedim
c2 = Circle(5)

print(f"c1: alan = {c1.alan_hesapla()}, çevre = {c1.cevre_hesapla()}")
print(f"c1: alan = {c2.alan_hesapla()}, çevre = {c2.cevre_hesapla()}")

