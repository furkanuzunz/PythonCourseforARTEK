numbers = [1,2,3,4,5]
#elimizde liste varken for ile bunları yazdirmak cok kolaydi
#ama misal ben 1-100 arasi sayilari yazdirmak istiyorsam nparım?????
# işte while kullanırım dostum manyak mısın what the fuuuuckk???

#1-100 e kadar
x = 0
# while True:
#     print(x)
#bu bize sonsuz döngü ürettirir moruk. cunku hep true olacak ve hep sıfırı yazacak

# while x < 100:
#     x = x+1
#     print(x)
# print("bitti...")

# while x < 100:
#     if(x % 2== 0):
#         print(x)
#     x = x+1
# print("ciftler bu kadar...")


# while x < 100:
#     if(x % 2== 0):
#         print(f"sayi cift: {x}")
#     else:
#         print(f"sayi tek: {x}")
#     x = x+1


#kullanicidan bir name degeri isteyelim kullanıcı girene kadar 
#onu isteyrlim.

name = "" #şöyleki aslında boşluk karakteri bize FALSE degerini dönderir.
#yani kullanici bir şey girerse biz bunu true ya cevirip döngüyü sonlandırabiliriz.

while not name.strip(): #False da yazabiliriz
#bosluk karakterini işleme almamak icin strip() methodunu kullanacaz.
    name = input("isminizi giriniz")
    
print(f"Merhaba, {name}")