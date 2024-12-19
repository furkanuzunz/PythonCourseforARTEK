"""
daire alanı  : pr^2
daire çevresi : 2pr

* yarıçapı verilen bir dairenin alan ve çevresini hesaplayınız
"""


r = float(input("yaricap : "))
pi = 3.14
alan = pi*(r**2)
print(type(alan))

cevre = 2*pi*r
print(type(cevre))

print("alan: " + str(alan) + " çevre : " + str(cevre)) #burada eger alan ve cevreyi stringe donustrumezsek birlesme islemi hata verir. cunku floatla stringi 
#birlestiremeyiz.