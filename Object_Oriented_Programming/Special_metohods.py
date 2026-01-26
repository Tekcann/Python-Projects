myList = [1,2,3,]
myString = "my String"

print(len(myList))
print(len(myString))
print(type(myList))
print(type(myString))

class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duraction = duration
        print("movie pbjesi oluşturuldu")
    def __str__(self):
        return (f"{self.title} by {self.director}")

    def __len__(self):
        return self.duraction
    
    def __del__(self):
        print("film silindi")


m = Movie("film adı", "yönetmen adı", 120)
# print(len(m)) # Movie objesi için len mtodu yoktur hata verir

print(type(m))

print(str(myList))
# ekrana yazdırma işlemlerini str metoduna kendimiz atabiliyoruz
print(str(m)) 
# metodu tanımlamadan önce adres yazdırırdı
# artık metonda gönderdiğimiz ifaseyi yazdırıyor

print(len(myList))
print(len(m))

# del metodonu kullanmasak bile bir süre sonra abje kendiliğinden bellekten silinir
# ancak del metodu ile biz manuel olarak silebiliriz

del m # obje silme işlemi

# print(m) # silindiği için hata verir



