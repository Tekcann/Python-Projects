liste  = ["1", "2", "5a", "10b", "abc", "10", "50"]

# 1. soru
# Bütün listeyi tarar eğer sayı değilse hata fırlatır 
# ve sonraki sayıya geçer eğer sayı ise bunu ekrana yazdırır
for x in liste:
    try:
        result = int(x)
        print(result)
    except ValueError:
        continue


# 2. soru

while True:
    sayi = input("Sayı: ")
    if (sayi == "q"):
        break
    
    try:
        result = float(sayi)
        print(f"girdiğiniz sayi: {result}")
    except:
        print("geçersiz sayı")
        continue

# 3. soru
turkce_karakterler = "şçüöıİ"

parola = input("parola: ")

for i in parola:
    if (i in turkce_karakterler):
        raise TypeError("Parola türkçe karakter içeremez")
    else:
        pass
print("geçerli parola")

# 4. soru Faktoriyel
def faktoriyel(x):
    x = int(x)

    if(x < 0):
        raise ValueError("Negatif değer")
    
    result = 1

    for i in range(1, x + 1):
        result *= i

    return result


for x in [5, 10, 20, -3, "10a"]:
    try:
        y = faktoriyel(x)
    except ValueError as e:
        print(e)
        continue

    print(y)