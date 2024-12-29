# 1-girilen 2 sayidan hangisi buyuktur

# a = int(input("a:"))
# b = int(input("b:"))

# result = (a > b)
# print(f"a : {a} b: {b} den buyuktur: {result}")

# 2- kullancııdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız
# eğer ortalama 50 ve üstündeyse gecti değilse kaldı yazdırın

# vize = int(input("vize:"))
# final = int(input("final:"))
# ortalama = (vize*(3/5)) + (final*(2/5))
# if(ortalama >= 50):
#     print("gecti")
# else:
#     print("kaldi")


# 3-girilen sayinin tek mi cift mi oldugunu yazdırın

# a = int(input("a:"))

# if(a%2 ==0):
#     print("cift sayi")
# else:
#     print("tek sayidir")

# 4-parola ve email bilgisini isteyip dogrulugunu kontrol ediniz.
email = "fuzun096@gmail.com"
password = "hello"

ema = input("email giriniz:")
passo = input("passo giriniz:")

if(email == ema.lower().strip() and password == passo): #emailde büyük kucuk harfe önem vermiyosan hepsini küçükten devam edersin.
    #ve de bosluk karaktelreirni de boşvereceksen strip methodunu kullanacaz
    print("giris basarili")
else:
    print("giris basarisiz")

    