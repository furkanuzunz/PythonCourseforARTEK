def changeName(n):
    n = "ada"
    print(n)
    
name = "furkan"

changeName(name)
print(name)
#name degismez cunku ikisi de bellegin farklı yerlerinde tanimlnamiştir.


def change(n):
    n[0] = "istanbul"
    
sehirler = ["ankara","izmir"]

change(sehirler)
print(sehirler)
#bu islemi yaptigimizde sehirler listesinin aslinda baslangic adresini
#gönderiyoruz.sonra bu fonksiyon bunun sıfırıncı indeksine girip onu "istanbul"
#ile degisir.


def add(a,b,c=0):
    return sum((a,b,c))

print(add(2,3))
print(add(2,3,4))

#mesela
def add2(*params):
    print(params)
    return sum(params)
# Python'da *params ifadesi, fonksiyona bir dizi değişken
# sayıda bağımsız değişken göndermenin bir yoludur.
print(add2(10,20,60))

#ya da---

def add3(*params):
    print(type(params)) #tuple tipidir.
    sum = 0
    
    for n in params:
        sum = sum + n
    return sum
print(add3(10,20,50))

def displayUser(**args):
    print(type(args)) # dictinory ye denk gelir.
    for key,value in args.items():
        print("{} is {}".format(key,value))
# **args kullanımı: Fonksiyonun parametre listesinde çift yıldız (**) ile gelen bir isim, fonksiyona anahtar-değer çiftleri olarak
# geçen tüm ek argümanları bir sözlük içinde toplar.

displayUser(name = "furkan",age = 2,city = "istanbul")
displayUser(name = "osman",age = 3,city = "samsun",phone = "12345")
displayUser(name = "osman",age = 3,city = "samsun",phone = "12345",email = "fuzun096@gmail.com")

#eğer tek bir liste göndereceksek tuple gibi tek yıldız kullanacaz
#ancak bir key value gibi dictionary felan göndereceksek de ve bunlarda
#farklı sayıda ve türde parametreler seklinde gitsin isitiyosak ** kullaniriz.

    
def myfunc(a,b,*args,**keywordargs):
    print(a)
    print(b)
    print(args)
    print(keywordargs)
    
myfunc(10,20,30,40,50,key1 = "value 1",key2 = "value 2")
# 30,40,50 yi tuple gibi aldı keyleri ise dict gibi
