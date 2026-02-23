# error handling => hata yönetimi

try:
    x = int(input("x: "))
    y = int(input("y: "))

    print(x/y)

# except ile hatanın ismini yazıyoruz 
# ve o hata oluşursa alt komutları çalışıryor
except (ZeroDivisionError, ValueError):
    print("Hatalı Giriş Yaptınız")

# ***YA DA***
# except ZeroDivisionError:
#     print("Hiç Bir Sayı Sıfıra Bölünemez")

# except ValueError:
#     print("Sadece Sayı Giriniz")

while True:
    try:
        x = int(input("x: "))
        y = int(input("y: "))

        print(x/y)
        
    # Exception as e -bu komut hatayı değişkenin içeriisne atar
    except Exception as e: 
        # eğer bir şey yazmazsak her hatada çalışır
        print("Hatalı Giriş Yaptınız\n", e)

    else: # eğer except komutu çalışmazsa esle komutarı çalışır
        break

    finally:
        print("try except sonlandı. Kod her zaman son bulur")


