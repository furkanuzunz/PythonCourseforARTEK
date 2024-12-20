names = ["Ali","Yağmur","Hakan","Deniz"]
years = [1998,2000,1998,1987]

#1- "Cenk" ismini listenin sonuna ekleyiniz
names.append("Cenk") 
names.insert(-1,"cenk") #insert fonksiyonu bizden bir indeks ister v eo indeksten önce koyar
print(names)
#2- "Sena" degerini listenin basina ekleyiniz
names.insert(0,"Sena") 
print(names)
#en sona isim eklemek istersek de len methodu ile en son şwyi bulup ondan önce ekleyebiliriz.

names.insert(len(names),"Furkan")
print(names)

#3- "Deniz" ismini listeden siliniz
#names.remove("Deniz")
#print(names)
#ya da pop methodu bir şey vermediğimiz zaman en son indekstekini siler.ya da belirlediğimiz indekstekini siler.

#4- "Ali" listenin bir elemanı mıdır?

isThere = names.index("Ali")
print(isThere)

#------ya da-----

result = "Ali" in names
print(result) #true ya da false döndürür bu bize


#5- "Deniz" isminin indeksi nedir?

indeksDeniz = names.index("Deniz")
print(indeksDeniz)

#6- Liste elemanlarını ters çevirin

#print(names[::-1])
names.reverse()
print(names)

#7- Liste elemanlarını alfabetik olarak sıralayınız

names.sort()
print(names) 

#8- Years listesini rakamsal büyüklüğe göre sıralayınız

years.sort()
print(years)

#9- str = "Chevrolet,Dacia" karakter dizisini listeye ceviriniz

str = "Chevrolet,Dacia"
result2 = str.split(",")
print(result2)

#10- years dizisinde kac tane 1998 degeri vardır ?

print(years.count(1998))

#11- years dizisinin en büyük ve en küçük elemanı nedir?

print(min(years))
print(max(years))

#12- years dizisinin tüm elemanlarını siliniz

years.clear()
print(years)

#13- kullanıcıdan alacagınız 3 tane marka bilgisini bir listede saklayınız.,

markalar = []

marka = input("Marka: ")
markalar.append(marka) #girilen markayı listemize ekledik.

marka = input("Marka: ")
markalar.append(marka) #girilen markayı listemize ekledik.

marka = input("Marka: ")
markalar.append(marka) #girilen markayı listemize ekledik.

print(markalar)
