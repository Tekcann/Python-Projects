# Inheritance (kalıtım) : Miras alma

# Peron => name, lastname, age, eat(), run(), drink()

#student ve teacher classları person clasının özelliklerine sahip olmasını
# istiyoruz yani Miras alma işlamini yapması oluyor

# student(Person) ek olarak öğnci sumarası gibi ek özelliklerde olucak, Teacher(Person)

# Class => class,        class
# animal => Dog(animal), Cat(animal)

class Person():
    def __init__(self, name, surname):
        self.firstName = name
        self.lastName = surname
        print("Person Created")
    def who_am_i(self):
        print(f"I am a Person")

    def eat(self):
        print("I am Eating")




# Miras aldığında Person'un init metodu çalışıyor
class Student(Person):
    # özellik elklemi şilemini tekrar yazmamıza gerek yok parametreleri verdiğimizde
    # inheritance işlemi gerçekleşir ve persun init komutu çalışır
    def __init__(self, name, surname, number):
        Person.__init__(self, name, surname)
        # eğer bu komutu yazmassan Student taki print komutu persondaki print komutu ezer.
        self.studentNumber = number
        print("Student Craeted")

    # override
    def who_am_i(self):
        print("I am a Student")

    def sayHello(self):
        print("Hello I am a student")


class Teacher(Person):
    def __init__(self, name, surname, branch):
        super().__init__(name, surname) # gene aynı işlev olur
        self.branch = branch
        
    def who_am_i(self):
        print(f"I am a Teacher and my branch {self.branch}")



p1 = Person("Ahmet", "Tekcan")
s1 = Student("Süleyman", "Soylu", 79)
t1 = Teacher("Tuğçe", "Demirçivi", "Meslek")

print(f"{p1.firstName} {p1.lastName}")
print(f"{s1.firstName} {s1.lastName} {s1.studentNumber}")

p1.who_am_i()
# dolaylı olarak Person metotlara student objeleri ulaşabiliyor
s1.who_am_i()
# eğer class larda aynı isimde metotlar varsa 
# aynı isimde ki metot temel class taki metodu ezer ve o çalışır

p1.eat()
s1.eat()

s1.sayHello()

t1.who_am_i()

