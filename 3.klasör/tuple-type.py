
list_ = [1,2,3]

tuple_ = 1,"iki",3 #ister böyle ister (1,"iki",3) böyle de tanımlanabilir

print(type(list_))
print(type(tuple_))

print(list_[2])
print(tuple_[2])

#suank var olan elemanları direkt değiştirebiliriz mesela.::::

list_ = ["ALİ","VELİ"]
tuple_ = ("damla","ayşe")

print(list_) #var olanları direkt degistik bir sey eklemedik yani direk icerikleri yeniledik gibi düşün
print(tuple_)

#bak mesela list[0] = "Ahmet" dersek ALİ ? ahmet ile degisir okey ama tuple da yaparsak 
#hata alırız.Tuple'da atandıktan sonra herhangi bir elemanını degisemeyiz.Tamamen icerigini degisebiliriz o okey
# ama atama işlemini yapamayız listedeki gibi.
#tuple üzerinde zaten iki tane method kullanabiliyoruz zaten listede ise bisürü method var

names = ("demet","emel","ayşe") + tuple_
print(names)


 