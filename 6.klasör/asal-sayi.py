'''
soru: girilen bir sayinin asal sayi olup olmadıgını bulun
asal sayi 1 ve kendisi haric tam böleni olmayan sayilara denir
'''

sayi = int(input("lutfen kontrol edilmesini istediginiz sayiyi giriniz:"))
i = 2
asalMi = True

if sayi == 1:
    print("1 sayisi asal değildir")

while(i < sayi //2):
    if(sayi%i == 0):
        asalMi = False
        break
    i+=1

if asalMi:
    print("girdiiginiz sayi asaldir")
else:
    print("girdiğiniz sayi asal değildir")
    
    
    #while yerine for i in range(2,sayi)
    #seklinde de yapabiliriz.# range methodu bu yüzden var
    
    