name = "Furkan"
surname = "Uzun"
age = 22
deneme = "My name is "


greeting = deneme + name + " " + surname + " and \n I am " + str(age) + " years old"

print("My named is " + name + " " + surname)
print(deneme + name + " " + surname + " and \n I am " + str(age) + " years old")  
#age ın basına gene str yazarız cunnku kendisi bi int ama biz string
#birlestirme islemi yapıyoruz---------İster tanımlama yaparken age = '22' seklinde tanımla istersen de str yazarak type casting yap.

print(greeting)

#diziler index index tutulur bellekte ve biz bunlara kraket parantezlerle ulasırız.

print("\n\t" + greeting[0]) #bunun ile M harfinin cıkmsı lazım. 
print("\n\t" + greeting[1])
print("\n\t" + greeting[2]) #bu mesela bosluk olcak
print("\n\t" + str(len(greeting))) #bu bize dizinin uzunlugunu veren methoddur/fonksiyondur.
length = len(greeting)
print("\n\t" + greeting[length - 1])   # bu bize bütün dizinin son karakterini yazdırır. neden -1 yaptık ? cunku diziler sıfırdan baslıyor
# eğer - 1 demeseydik program bellekte rastgele bir yere ulasıcaktı farklı degerler verecekti. ondan.

# eğer belli bir indeksten basla belli bir indekse git demek istiyorsam ;

print(greeting[3:7]) # 7 dahil değil mesela .

#eğer bi yerden baslatip sonuna kadar gitmesini istersem ;

print(greeting[3:]) #3.indeks olan nameden baslar ve devam eder sonuna kadar.

# ya da mesela bastan belirli bi son karaktere kadar devam etmesini istersek

print(greeting[:15]) #bastan baslayıp 15.karaktere dek devam eder.

# vov vov vov muhteşem bi özellik bu c dilinde çok zor olurdu mesela derdikki o stringin her indeksini eğer 2 ye kalan sıfırsa al ve yazdır değilse yazdırma
#seklinde yapardık. pythonda ise bu direkt asagıdaki sytnaxla oluyor.

muhtesem = greeting[2:40:2] #demek 2.indeksten basla 40.indekse kadar ama 2 karakterde bir al demektir.
print(muhtesem)


