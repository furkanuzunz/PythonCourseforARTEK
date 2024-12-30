sayilar = [1,3,5,7,9,12,19,21]

# 1- sayilar listesini while ile ekrana yazdirin 

# x = 0
# while (x < len(sayilar)):
#     print(sayilar[x])
#     x+=1


# 2- Baslangic ve bitis indeks  degerlerini kullanicidan alip aradaki tüm tek
#yukaridaki sayilar listesinden bagimsiz bu  sayilari ekrana yazdirin.

# baslangic = int(input("baslangic:"))
# bitis = int(input("bitis:"))

# i = baslangic
# while i < bitis:
#     i += 1
#     if i % 2 ==1:
#         print(i)
    
# 3- 1-100 arasindaki sayilari azalan sekilde yazdirin

# sayac = 100
# while sayac > 1:
#     print(sayac)
#     sayac-=1

# 4- kullanicidan alacaginiz 5 sayiyi ekranda sırali bir şekilde yazdirin

# numbers = []
# i = 0
# while i < 5:
#     number = int(input("sayilari giriniz lütfen"))
#     numbers.append(number)
#     i+=1

# numbers.sort()
# print(numbers)

#print(numbers.sort()) bu sekilde none döndürür önce sıralatıp sonra yazdirmamiz gerekir.


# 5-Kullanicidan alacaginiz sinirsin ürün bilgisini ürünler listesi icinde
# saklayiniz
# ** urun sayisini kullaniciya sorun
# *** dictionary listesi yapisi (name,price) şeklinde olsun
# ****urun ekleme işlemi bittiğinde urunleri while ile listeleyin

urunler = []

adet = int(input("kac ürün eklemek istiyorsunuz?"))
i = 0
while i<adet:
        name = input("urun ismi:")
        price = input("urun fiyati:")
        urunler.append({
            "name":name,
            "price":price
        })
        i += 1
print(urunler)

for urun in urunler:
    print(f"urun adı: {urun["name"]} urun fiyati {urun["price"]}") #fiyatida string yazmamizinsebbei input methodu string olarak aliyor.
# Neden Tırnak İşaretleri İçinde Yazmalıyız?
# Anahtarlar ve Değerler: Python sözlüklerinde (dictionary), anahtarlar ve
# değerler çiftler halinde saklanır. Anahtarlar string, integer, 
# tuple gibi çeşitli veri tiplerinde olabilir, ancak string anahtarlar 
# kullanıldığında tırnak işaretleri gerekir.

# Sözlük Elemanlarına Erişim: Sözlükteki elemanlara erişirken, string anahtarları tırnak işaretleri
# içinde kullanmak zorundayız. Bu, Python'un anahtarın bir string olduğunu anlamasını sağlar.