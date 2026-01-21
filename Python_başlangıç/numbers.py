maasAli = 5000
maasAhmet = 4000
vergi = 0.27

print(maasAli - (maasAli * vergi))
print(maasAhmet - (maasAhmet * vergi))

#değişekn tanımlama kuralları
#sayısal ifade ile başlayamaz
#türkçe ifadeler değişkenlerde tanımlama

x = 1               #int
y = 1.1             #float
name = "Meliha"     #sring
is_student = True   #bool
#ya da ************************
#bu komutta çalışır  ve mantıklı

x,y,name,is_student = (2,2.2,"Adana", False)


a = '10'
b = '20'
print(a + b) # 30 olmaz => 1020 yazar
