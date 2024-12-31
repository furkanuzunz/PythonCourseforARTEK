# #1- Gonderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın

# def name(name,kac_kez):
#     i = 0
#     while i < kac_kez:
#         print(name)
#         i+=1
# name("furkan",5)
# #2- Kendine gönderilen sınırsız sayidaki parametreyi bir listeye ceviren fonksiyon

# def sinirsiz(*params):
#     print(list(params))

# sinirsiz(10,20,30,"furkan")

# #-----ya da --------

# def listeyeCevir(*params):
#     liste = []
    
#     for param in params:
#         liste.append(param)
#     return liste

# heyo = listeyeCevir("furkan",10,20)
# print(heyo)
#3- Gonderilen 2 sayı arasındaki tüm asal sayilari bulan fonksiyon

# a = int(input("sayi 1:"))
# b = int(input("sayi 2:"))
# def asalSayi(a,b):
#     for sayi in range(a,b+1):
#         if sayi > 1:
#             for i in range(2,sayi):
#                 if(sayi % i == 0):
#                     break
#             else:#ifin icinde tüm bölenler kontrol edildikten sonra cikip else ile yazdiriliyor o yüzden ele bi tab geride
#                 #yani icteki forun icinde degil dıstaki forun icinde olmali else
#                 print(sayi)
    
# asalSayi(a,b)

# for-else Yapısı:

# Döngünün hiçbir break ile kesilmeden tamamlanması durumunda çalışır.
# else, doğrudan döngünün tamamlanmasıyla ilgilidir, if ile doğrudan bağlantılı değildir.
#4- Kendisine gönderilen bir sayinin tam bölenlerini bir liste şeklinde döndür

a = int(input("sayiyi giriniz"))
def bolenler(sayi):
    i = 1
    liste = []
    while i < sayi: # ya da for i in range(2,a) yapabilirisn.
        if(sayi % i == 0):
            liste.append(i)
        i+=1
    print(liste)
bolenler(a)


