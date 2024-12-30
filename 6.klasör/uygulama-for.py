sayilar = [1,3,5,7,9,12,19,21]

#1-sayilar listesindeki hangi sayilar 3 ün katidir?
for sayi in sayilar:
    if(sayi%3 == 0):
        print(sayi)


#2-Sayilar listesinde sayilarin toplami kaçtir?
toplam = 0
for sayi in sayilar:
     toplam += sayi
print("toplam:",toplam)


#3-sayilar listesindeki tek sayilarin karesini aliniz?
for sayi in sayilar:
    if(sayi % 2==1):
        print(sayi**2) 


sehirler = ["kocaeli","istanbul","ankara","izmir","rize"]

#4- Şehirlerden hangileri en fazla 5 karakterlidir?

for sehir in sehirler: #her sehire bir sey atandıgında aslında kocaeli atancak mesela öyle düşün.
   if (len(sehir) <= 5):
       print(sehir) 
urunler = [
        {"name":"samsung S6", "Price":"3000"},
        {"name":"samsung S7", "Price":"4000"},
        {"name":"samsung S8", "Price":"5000"},
        {"name":"samsung S9", "Price":"6000"},
        {"name":"samsung S10", "Price":"7000"}
] #suanda her bir sözlük tipi liste icinde . altta listeden cıkartılıp yazdırılır her biri tamamen görükür sadece key değil mesela.

#5- Ürünlerin fiyatları toplam nedir?
#biz diyelim fiyat bilgisiyle ilgileniyosak print(urun["price"]) yazdirinca fiyatı verir bize
for urun in urunler:
    print(urun["Price"])

toplam = 0
for fiyatlar in urunler:
    toplam += int(fiyatlar["Price"])
print(toplam)       


#6- Ürünlerin fiyatı en fazla 5000 olan ürünleri gösteriniz?

for urun in urunler:
    if (int(urun["Price"])<= 5000):
        print(urun["name"])


#for dongusu ile genel olarak liste üzerinde dolaşiyoruz.