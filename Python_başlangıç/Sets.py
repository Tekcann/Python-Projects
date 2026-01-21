fruits = {"orange", "apple", "banana"}

#print(fruits[0]) //indexlenemez

#genede index numaraları yok
for x in fruits:
    print(x)

#eleman eklemek için yol
fruits.add("cherry")

#aynı eleman iki kere eklenmiyor
#ama tek seferde birden fazla eleman ekleyebiliriz
fruits.update(["mango", "grape", "apple"])

print(fruits)

myList = [1,2,5,4,4,2,1]
#bir dizide aynı elemanlar var

print(myList)#bu şekilde bütün elemanları yazdırır

print(set(myList))#aynı elemanları tek sayar ve ikinci defa yazmaz
#ve sanırım elemanları küçükten büyüğe sıralıyor

fruits.remove("mango")#eleman silme isşlemi
fruits.discard("apple")#eleman silme işlemi

fruits.pop()
#bu şekilde kullanılırsa herhangi bir elemanı siler.şans

fruits.clear()#bütün elemanları siler

print(fruits)

