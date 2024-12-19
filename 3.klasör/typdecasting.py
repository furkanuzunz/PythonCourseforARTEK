# # #input methodu bize kullanıcıdan bir girdi almamızı sağlar
# # ### şunu unutmamak lazım inputla aldıgımız bir deger string olarak alinir. bunun icin mesela ben 2 ve 3 sayilarini girersem cıktı 5 degil 23 olucak
# # # bunun icin yapmamiz gereken * x ve y yi type casting yaparak int degere dönüştürmemiz lazım(aşağıdaki gibi)   

# # """
# # sebebi :
# # kullanıcıdan alınan verinin belirsizliği:
# # Kullanıcıdan alınan veri, her zaman metin (string) formatında kabul edilir çünkü kullanıcı doğrudan bir metin girişi yapar. 
# # Klavye ile girilen her şey, sayı, harf veya özel karakterler olsun, en temel şekilde metin olarak alınır.
# # """


# # x = input('1.sayi :')
# # y = input('2.sayi: ')

# # print(type(x))
# # print(type(y))

# #  #tiplerini yazdırdım  görebilmek için

# # toplam = int(x) + int(y)   


# # print(toplam)

# # # ctrl-k ve ctrl -c ile hepsi yorum satiri 
# # # ctrl k ve ctrl u ile hepsi geri alınır



x = 2.5
y = 4
name = "Çınar"
isOnline = True 

# # print(type(x))
# # print(type(y))
# # print(type(name))
# # print(type(isOnline))

# # type casting 

# # x = float(x)
# # print(x)
# # print(type(x))

# # y = float(y)
# # print(y)
# # print(type(y))

# result = str(x) + str(y)
# print(result)
# print(type(result))


# isOnline = str(isOnline)
# print(isOnline)
# print(type(isOnline))

isOnline = int(isOnline)
print(isOnline)
print(type(isOnline))