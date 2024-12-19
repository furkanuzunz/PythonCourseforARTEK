website = "http://www.sadikturan.com"
course = "Python Kursu : Baştan sona Python programlama rehberiniz (40 saat)"

# 1- "course"  dizisinde kaç karakter bulunmaktadır.
length = len(course)
print(length)

# 2- "website" içerisinden www karakterlerini alın.

kaldirmak = website.replace("www","")
print(kaldirmak)

almak = website[7:10]
print(almak)

# 3- "website" içerisinden com karakterlerini alın.

kaldirmak2 = website.replace("com","")
print(kaldirmak2)

almak2 = website[22:25]
print(almak2)

length2 = len(website)
print("*",website[length2-3:length2])

# 4- "course" içinden ilk 15 ve son 15 karakterlerini alın
length = len(course)
onbesmevzusu = course[14:length]
print(onbesmevzusu)

# İlk 15 karakteri alıyoruz
ilk_15 = course[:15]

# Son 15 karakteri alıyoruz
son_15 = course[-15:-1]  #son indeksi dahil etmez.

print("İlk 15 karakter:", ilk_15)
print("Son 15 karakter:", son_15)

# 5- "course" ifadesindeki karakterleri tersten yazdirin.

##sol tarafa : ekleyince baslangıc karakterleri sağ tarafa : eklersek son karakterlerle isimiz olur. hepsiyle isimiz olursa da :: ekleriz.
## sadece course[::] yapsak normal hepsi yazdırılır.
## eğer course[::2] yaparsak hani snaki 2 adımda bir yazdır gibi anlam cıkar.
## bir yazınca da mesela direkt normal yazıyor o zaman -1 yazınca da tersten yazıyor.



tersten = course[::-1]
print(tersten)

s = '12345' *5  # bu 5 kere 12345 stringini yazdırır.
print(s) #burda ise 5 tane 12345 dir.
# mesela ben sadece 5 şeyde bir al derseö
print(s[::5]) #ciktisi 11111 dir.


#---------------------------------------------------

name, surname, age,job = 'Bora','Yilmaz',32,'muhendis'

# 6- Yukarıda verilen degiskenler ile ekrana asagıdaki ifadeyi yazdıırn
    #   'Benim adım Bora yılmaz , Yaşım 32 ve mesleğim mühendis.


fullname = "Benim adim " + name + surname + "," + " Yasim " + str(age) + "ve mesleğim " + job
print(fullname)
another = "Benim adım {} {} , Yaşım {} ve mesleğim {}.".format(name,surname,age,job)
another2 = f"Benim adim {name} {surname} , Yaşım {age} ve mesleğim {job}"
print(another)    
# 7- "Hello world " ifadesindeki w harfini  'W' ile degistirin 

hey = "Hello world"
neresi = hey[6]
print(neresi)

hey2 = hey[:6] + "w" + hey[7:]  ## ya da hey[:6] + "w" + hey[-4:]

 ## ya da replace methodu ile yapariz.
print("*",hey.replace("W","w"))
print(hey2)
# 8- 'abc' ifadesini yan yana 3 defa yazdirin.

heyo = "abc "
print(heyo*3)