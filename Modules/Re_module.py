import re

result = dir(re)

# reguler expression
# bir metin içindeki belirli karakter kalıplarını
# veya şablonları bulmak, değiştirmek ya da doğrulamak
# için kullanılan bir "arama filtresi" dilidir.

 

# re modülü

str = "Python Kursu: Python Programlama Rehberiniz | 40 saat"

# re.findall()
# değişkenin içerisinde istenilen ifade var mı diye bakar
result = re.findall(("Python"), str)

# re.split()
# istenilen ifadeden değişkeni böler
result = re.split(" ", str) # mesala boşluk

# re.sub()
# değiştirme işlemi

result = re.sub(" ", "-", str)
# prametreler: değiştirilecek ifade, yerine geçeçek olan,
# değişikliğe uğrayacak değişken

# re.search()
# değişkende arar ve ilk bulduğu kısmı mach olarak döndürür
mach_objesi = re.search("Python", str)

result = mach_objesi.span() #kaçıncıendexte olduğunu söyler (çıkıtı: (0, 6))

result = mach_objesi.start() # başlangıçendexi
result = mach_objesi.end() # bitişendexi


result = mach_objesi.group() # aranan kelimeyi dödürür

result = mach_objesi.string # aranılan değişkenin döndürür


# REGULER EXPRESSİON

"""
    [] - Köşeli parantezler arasında yazılan bütün karakterler
         aranır. harfharf bakar

         [abc] => a     :1 match
                  ac    :2 match
                  Python:no match

        [a-e] => [abcde],
        [1-5] => [12345],
        [0-39] => [01239]
        
        [^abc] => abc dışındaki karakterler
        [^0-9] => rakam olmayan karakterler

"""

result = re.findall("[abc]", str) 
# karakterleri ayrı olarka arar
result = re.findall("[saat]", str)

result = re.findall("[a-e]", str) 
# a-e dahil arasındakş kelimerli arar

result = re.findall("[1-5]", str)

result = re.findall("[^abc]", str) 
# abc dışındakileri döndürür

"""
    . -Her hangi bir tek karakteri belirtir

        .. => a     : No match
              ab    : 1 match
              abc   : 1 match
              abcd  : 2 match

"""

result = re.findall("...", str) 
# boşluk dahil her şeyi 3 gruba ayırır


result = re.findall("Py..on", str)


"""
    ^ - Belirtilen değişken karakterle başlıyor mu?

        ^a => a     :1 match
              abc   :1 match
              bac   :NO match

"""

result = re.findall("^P", str)
# verilen değişkenin en başındakini kontrol eder

"""
    $ - Belirtilen karakterle bitiyor mu?
        a$ => a     :1 match
              lamba :1 match
              Python:NO match

"""

result = re.findall("t$", str)
# verilen değişkenin en sonundakini kontrol eder
result = re.findall("saat$", str)


"""
    * - bir karakterin sıfır ya da daha fazla
        sayıda olmasınıkontrol eder

        ma*n => mn    :1 match
                man   :1 match
                maaan :1 match  
                main  :NO match  

"""

result = re.findall("sa*t", str)

"""
    + - Bir karakterin bir ya da daha fazla sayıda olmaasını
        kontrol eder.

        ma+n => mn    :NO match
                man   :1 match
                maaan :1 match
                main  : NO match(a' nın arkasından n gelmiyor)

"""

result = re.findall("sa+t", str)


"""
    ? - bir karakterin sıfır ya da bir kez
         olmasını kontrol eder

        ma?n => mn    :1 match
                man   :1 match
                maaan :NO match  
                main  :NO match (a' nın arkasından n gelmiyor)

"""

result = re.findall("sa?t", str) # iki a var o yüzden olmz

"""
    {} - Karakter sayısını kontrol eder

        al{2} => a karakterinin arkasına 1 karakteri 2 kaz tekrarlamalı
        al{2,3} => a karakterinin arkasına 1 karakteri en az 2 en fazla 3 kez tekrarlamalı
        [0-9]{2-4} => en az 2 en çok 4 basaklı sayılar
"""


result = re.findall("a{2,3}", str)
result = re.findall("[0-9]{2,3}", str)

"""
    | - alternatif seçeneklerden birinin gerçekleşmesi gerekir

        a|b => a yada b

            cde     :NO match
            ade     :1 match
            acdbea  :3 match     

"""

"""
    () - gruplamak için kullanılır

        (a|b|c)xz => a,b,c karakterinin 
                 arkasına xz gelmelidir
"""

"""
    \ - Özel karakterleri aramamızı sağlar.
        \$a => $ karakterinin arkasına a karakterini arar.
        Yani $ regular exp. engine tarafından yorumlanmaz.

    \A - Belirtilen karakter string en başında mı?
        \Athe => the string en başındamı

    \Z - Belirtilen karakter string en sonunda mı?
        the\Z => the string en sonunda mı

    \b - Belirtilen karakter kelimenin en başında ya da sonunda mı?
        \bthe = the kelimesinin en başında mı?
        the\b => the kelimenin en sonunda mı?

    \B - Belirtilen karakter kelimenin en başında ya da sonunda değil mi?
        \Bthe => the kelimenin en başında değil mi?
        the\B => the kelimenin en sonunda değil mi

    \d - [0-9] ile aynı anlama gelir yani rakamları arar

    \D - [^0-9] ile aynı anlama gelir yani rakam olmayanları arar


    \s - Boşluk karakterini arar
    \S - Boşluk karakteri dışındakiler
    \w - Alfabetik karakterler, rakamlar ve alt çizgi karakteri
    \W - \w nin tam tersi

    
    ***DÖKÜMANTOSYONLARI İNCELE EZBERLEMEK ZORUNDA DEĞİLSİN***
"""


print(result)

