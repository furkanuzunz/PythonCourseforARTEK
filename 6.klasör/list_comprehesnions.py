numbers2 = []
for x in range(10):
    numbers2.append(x)
print(numbers2)
    
  
#bunun daha kolayi var

#ya iste aldigimiz değerleri önce tek tek x e attik sonra onu direkt x değerine atadik listeyi onu da numbersa esitledik.x in icindeki degerler listenin (dizinin)icindekidegerleri temsil ediyor.
#iki tane x kafamizi karistirmasin aldiğimiz x leri soldaki x de kullaniyoruz aslinda
numbers = [x for x in range(10)]  #range ile teker teker rakam elde edip bunu x içerisine atiyouz ve ,
#bir x değeri elde ediyoruz.ve bunu numbers içine yaptik
print(numbers)

for x in range(10):
    print(x**2)

numbers3 = [x**2 for x in range(10)]
print(numbers3)

numbers4 = [x*x for x in range(10)]
print(numbers4)
# ya da kendisinin 3 e bölümünden kalans ıfırsa karelerini al diyedebiliriz.
numbers5 = [x*x for x in range(10) if x%3 == 0]
print(numbers5)


#stringlerde nasıl olur peki ????

myString = "Hello"
myList = []

for letter in myString: #my stringin icinden gelen karakteleri tek tek lettera atadik sonrasinda bunu myList icerisine gönderip liste haline gönderdik.
    myList.append(letter)
print(myList)
#bunu daha basit bir sekilde yazdirabiliriz.
myList2 = [letter for letter in myString]
print(myList2)

years = [1983,1999,2008,1956,1986]
ages =  [2019 - year for year in years]
#aslında years'dan yeara bilgileri aktardik sonra da soda 2019 - year da da işlemlerimizi yaptik
print(ages)

#şöyle bir şey yapalim x çift ise direkt kendini yazşrsin değil ise else ile "TEK" diye yazdiralim.
results = [x if x% 2== 0 else "TEK" for x in range(1,10)]
print(results)

#iç içe döngü olursa nolucak
results2 = []

for x in range(3):
    for y in range(3):
        results2.append((x,y))
print(results2)

#peki bunu nasil basit bir sekilde yapabiliriz.

numbers6 = [(x,y)  for x in range(3) for y in range(3)]
#x icin fordakini (x,y) burada x kismina aldik y yi de y kismina

print(numbers6) 