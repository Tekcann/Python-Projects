import random


result = random.random() # Varsayılan 0.0 - 1.0 arası
result = random.random() * 100 # gelen sayıyı 100 ile çarpar

result = random.uniform(10,100) # 10 - 100 arası ondalık sayı üretir

result = random.randint(10, 100) # 10 - 100 arası int değer üretir


names = ["ali", "yağmur", "deniz", "cenk", "ahmet", "efe"]

result = names[random.randint(0, len(names) - 1 )]
# bu iki kodda aynı işlevi görür, diziden rasgele veri seçer
result = random.choice(names)

# kelimenin içerisinden rasgele bir harfi seçer
greeting = "Hello World"
result = random.choice(greeting)

# Sıralı olarak listenin içine atar
liste = list(range(10))

# bu komuuta dizinin iççindeki verilerin indexlerini karıştırır
random.shuffle(liste)
result = liste

liste = list(range(100))
result = random.sample(liste, 3) # dizinin içerisinde rasgele 3 veri alır
result = random.sample(names, 2)


print(result)