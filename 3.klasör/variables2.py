
# 1 --- bir musteri belirledik ve bunun hakkında degiskenlerin nasıl tanımlanabileceği üzerinde durduk

musteriAdi = "Furkan"
musteriSoyadi = "Uzun"
musteriId = musteriAdi + ' ' +  musteriSoyadi
musteriCins = True #erkek
musteriTc = '123456789' #saysıal olarak bununla ugrasmayacağımız için string olarak tanımlamakta fayda var
musteriDg = 2002
musteriAdres = "Motorunun üstü"
musteriAge = 2024 - musteriDg


"""
    Aşağıdaki siparişlerin toplam bilgisini hesaplayacağız

    sipariş1 = 110 TL
    sipariş2 = 1234.45 tl
    sipariş3 = 356.95 tl 

"""


order1 = 110
order2 = 1234.45
order3 = 356.95

#ya da total = order1 + order2 + order3 diyerek direkt totali yazdırabiliriz. print("total : ",total) diyerektten

print(order1 + order2 + order3)