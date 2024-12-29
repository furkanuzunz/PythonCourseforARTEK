#sets listelerini görücez

fruits = {"orange","apple","banana"}

# print(fruits[0])  bu sekilde kullanamzsin cunku sets objeji indekselenemz bir tiptir
#ayrıca sıralayamayız da
#elemanlarına for döngüsü ile ulaşıcaz.
for x in fruits:
    print(x)
    
fruits.add("cherry")

#birden cok elemanı ise update methodu ile içine liste göndererek ekleyebiliriz.
fruits.update(["mango","grape"]) #var olan elemanı eklesek bile tekrarlanmaz.küme gibi aslıdna

print(fruits)


myList = [1,2,3,3,4,5,6,6] #ben bunu set constructorına gönderirsem tekrarlayan elemanlar silinir
print(set(myList))


fruits.remove("mango")
fruits.discard("apple")

fruits.pop()         #normalde pop fonksiyonu hicbir indeks yazmadıgın zaman son elemanı silerdi ama burada fruits sıralanmıyor kendi icinde bu yüzden burada öyle olmaz.burada ilk eleman gider.

fruits.clear()#butun elemanlar silinir.

print(fruits)