# def cube():
#     # result dizisi bellekte yer tutar
#     result = []

#     for i in range(50000):
#         result.append(i**3)
#         return result
    
# print(cube())


# bellek üzerinde yer tutmayan bir yapı generator

def cube2():
    for i in range(50):
        yield i ** 3
        # anlık değeri yield ile gönderiyoruz (return gibi ama farklı;)

generator = cube2()
# generator artık itarable obje 
# işlevi: istediğimiz işlemler bellekte yer kaplamıyor ancak 
# bir istediğimizde ulaşabliyoruz ve sadece biz istediğimizde üretiliyor

iterator = iter(generator)

# next fonkistonunu kullnamamk için iterator olmalı
print(next(generator))


for i in iterator:
    print(i)

print(generator)



generator = (i**2 for i in range(5))

print(str(next(generator)) + "aa") # next komutu kullanıldıktan sonra 
# eğer bir daha eleman çağırırsak sonraki elemandan başlıyor

for i in generator:
    print(i)