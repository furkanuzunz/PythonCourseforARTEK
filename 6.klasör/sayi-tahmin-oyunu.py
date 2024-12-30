'''
1-100 arasindaki rastgele üretilecek bir sayiyi asagi yukar ifadeleri ile buldurmaya calisin
*random modülü için "python random"şeklinde arama yapin
**100 üzerinden puanlama yapin her soru 20 puan
*** hak bilgisini kullanicidan alin ve her soru belirtlien can sayisi
üzerinden hesaplansin
'''

import random

dogrusu = random.randint(1,10)
varSayilanhak = 5
can = int(input("kac hak kullanmak isterisniz:"))
hak = can
i = 0
while hak > 0:
    hak -= 1
    i+=1
    tahminEdilen = int(input("tahmininizi giriniz:"))
    if(tahminEdilen<dogrusu):
        print("tahminizi biraz büyültün")
    elif(tahminEdilen>dogrusu):
        print("tahminizi biraz kucultun")
    elif(tahminEdilen == dogrusu):
        print(f"tebrikler dogru bildiniz {i}. hakta bildiniz: puaniniz : {100 - (100/can) * (i - 1)}")
        break
    if varSayilanhak == 0:
        print(f"bilemediniz ve haklariniz tükendi tutuşlan sayi : {dogrusu}")
