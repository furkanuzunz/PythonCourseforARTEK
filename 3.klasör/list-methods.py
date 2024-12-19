numbers =  [1,10,5,16,4,9,10]
letters = ["a","g","s","b","y","a","s"]

minVal = min(numbers)
maxVal = max(numbers)
maxLet = max(letters)
minLet = min(letters)
print(minVal)
print(maxVal)
print(maxLet)
print(minLet)

val2 = numbers[3:6]
val3 = numbers[:3]
print(val2)
print(val3)


#### append methodu ile listenin üstüne eleman ekleyebiliriz.

numbers.append(49)
print(numbers)

#peki istedigimiz bir konuma    eleman ekleyebilir miyiz??? EVETT

# ınsert methodu ile yaparız onuda.

numbers.insert(3,78) #hangi indeksten önce eklemek istiyosak oraya yazarız.yani 3.indeksi sağa kaydırdı ve 78 eklendi
numbers.insert(-1,  23)       
print(numbers)

#pop() methodu listenin elemanını siler.
numbers.pop() #bu sekildeyken sondakini sildi
numbers.pop(0) #sıfırıncı indeksi de siler.
print(numbers)

#   remove  methodu ile de silmek istediğimiz numarayı/elemanı veririz o silinir.
numbers.remove(16) # tamamen bi arama yapar ve aradığı elemanı siler.
print(numbers)


##------SIRALAMA İŞLEMLERİ------

numbers.sort() ###---kucukten buyuge sıralar-----
letters.sort() ###----alfabetik olarak sıralar
print(numbers)
print(letters)
### ---- tersine döndermek icin REVERSE methodunu kullaniriz.
numbers.reverse()
letters.reverse()
print(letters)
print(numbers)

numbers.clear() ## bütün elemanları temizler.
print(numbers)