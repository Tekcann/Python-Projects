name = "Ahmet Tekcan"

# for letter in name:
#     if(letter == "t"):
#         break # döngüden tamamen çıkış yapar
#     print(letter)

# print("*" * 50)
# for letter in name:
#     if(letter == "t"):
#         continue # o anki döngü turunun iptal ediyor
#     print(letter)

# x = 0
# # x = 2 olduğu an 'break' komutu çalışır 
# # ve döngüyü bitirir 
# while (x < 5):
#     if (x == 2):
#         break
#     print(x)
#     x += 1

# x = 0
# # x = 2 olduğuda 'continue' çalışır ve dögüyü başa atar
# # ama döngü başa dönerken x in değeri değişmediği için döndü takılı kalır
# while (x < 5):
#     if (x == 2):
#        continue
#     print(x)
#     x += 1

# 1 den 100 kadar olan sayıların toplamı

x, toplam = 1, 0
while (x <= 100):
    toplam += x
    x += 1

print(toplam)