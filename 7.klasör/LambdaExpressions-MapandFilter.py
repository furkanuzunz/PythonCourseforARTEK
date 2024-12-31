#Lambda fonksiyonları görecez ve map ve filter methodlarını görecez lambda fonksiyonlarında

def square(num): return num **2

numbers = [1,3,5,10,9,4]

#map methodu ile dizi icerisindeki her elemani tek tek alıp fonksiyon icerisinden gecirebiliriz.
map(square,numbers)  #fonskiyonu yazarken cagırmıyoruz sadece ismini yaziyoruz.
result2 = map(square,numbers) #suan bu haldeyken bize bir adres dönderir bizim bunlari bir liste icine atmmaiz gerekiyor.
result = square(2)

result3 = list(map(square,numbers)) #suan iste listeye atar o sekilde verir.
#ya da mesela list e cevirmeden for dongusu ile de yapabiliriz.
for item in map(square,numbers):
    print(item)




print(result)
print(result2)
print(result3)

# map fonksiyonu Python'da bir iterator döndürür. Bir iterator, temelde, üzerinde yineleme yapılabilecek bir nesnedir. Ancak bu iterator doğrudan liste benzeri bir yapıya sahip değildir. 
# Bu yüzden, iterator'ı bir listeye çevirmeden print(result2) yazdığınızda, bellekteki konumunu temsil eden bir adres döner.

# Iterator, Python'da veri yapılarında yineleme (iterasyon) yapmayı sağlayan bir nesnedir. Daha basit bir ifadeyle, bir koleksiyon (örneğin, 
# liste, tuple, string) üzerinde tek tek elemanları dolaşmanıza imkan tanır.

#şimdi şöyle bir şey var sonuçta mapta ilk parametre kismi , 2.paramteredekileri tek tek alip oraya gönderip ne gerekiyorssa 
#o işlemleri yapiyor RİGHT? E O ZAMAN ben fonksiyon kullanmasam mesela kare almak icin fonksiyon kullanmasam da
# map methodunda 1.paramterre kismina işlemimi yazsam.
 
#ismi olmayan fonksiyon tanımlamak icin "lambda" kullancaz
result4 = list(map(lambda num : num **2,numbers))
print(result4)

lambdakullanimi = lambda num2 : num2 **2

result5 = list(map(lambdakullanimi,numbers))
print(result5)


#mesela ben karelerini aldim ya map ile teker teker gönderdim ama resulta gelen
# sonuclardan secmek istiyorum ciftleri gibi 
# filter metodu, bir iterable'ın (örneğin bir liste) elemanlarını belirli bir koşula göre süzmek (filtrelemek) için kullanılır. 
# filter fonksiyonu, bir fonksiyon ve bir iterable alır ve yalnızca verilen koşulu sağlayan elemanları içeren bir iterator döndürür.


def check_even(num): 
    return num % 2 == 0
 
result6 = list(filter(check_even,numbers))
print(result6)

#lambda ile kullanimi 
# Python'da lambda ifadesi, küçük ve tek satırlık anonim fonksiyonlar oluşturmak için kullanılır. Anonim fonksiyon, adlandırılmamış bir fonksiyondur. lambda fonksiyonları, 
# genellikle küçük işlevleri hızlıca tanımlamak istediğinizde kullanışlıdır.

result7 = list(filter(lambda num3:num3%2 == 0,numbers))
print(result7)