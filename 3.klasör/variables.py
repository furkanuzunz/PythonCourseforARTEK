maasALi = 5000
maasAhmet = 4000
vergi = 0.27
#maas bilgisi vs veritabanından gelen bilgiler olucak ileride.

print(maasALi - ( maasALi *vergi))
print(maasAhmet - (maasAhmet * vergi))

"""
  degisken tanımlama kurallari

  1-rakam ile baslayamaz
  ama mesela _number1 olur  
  2- aynı degisken ismini gene aynı kapsam icerisinde kullanamayiz  
    3- büyük kücük harf duyarlılığı vardır.
        yani age ve AGE degisken isimleri farklıdır.
    4- türkce karakter kullanılmaz
"""

number1=10
print(number1)
number1 = 20
print(number1)

number1 += 30
print(number1)

age = 20
AGE = 30

yaş = 20 #false
yas = 20 #correct

x = 2 #int
y = 2.4    #float
name = "Çinar" #string
isStudent = True #boolean tipinde 

x,y,name,isStudent = (2,2.4,"Çinar",True) #seklinde tek satirdada yazabiliriz.

a = 10
b = 20
print( a + b) #30

c = '10'
d = '30'
print(c + d) #1030 cevabı gelir cunku binevi string birleştirme işlemi yapıyoruz.cunku tırnak ile tanımladık bunu program string olarak tanımlar.

firtsName = "furkan "
lastName = "uzun"
print(firtsName + lastName)  #furkan uzun
