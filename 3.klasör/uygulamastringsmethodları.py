website = "http://www.sadikturan.com"
course =  "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- ' Hello World ' karakter dizisinin baş ve son boşluk karakterlerini silin
#-----strip-----
str = " Hello World "
str1 = str.strip()
str2 = str.lstrip()  #baştan soldaki boslugu siler
str3 = str.rstrip() #baştan sağdaki boslugu siler
str4 = website.lstrip(":/pth")
print(str4)
#istersek silmek istedigimiz **karakteri belirtebiliriz**parantez icinde.hicbirsey yazmazsak sadece bastaki boslugu siler.
print(str1)
# 2- website değişkenindeki sadikturan haricindeki bilgileri silin
soldan = website.lstrip(":/whtp.")
sagdanidasilinmishali = soldan.rstrip(".com") 
#ya da direkt olarak result = website.strip("w.moc") yaparak da olur.
print(sagdanidasilinmishali)
# 3- 'course' u tamamını kucuk harf yapın

kucultuldu = course.lower()
print(kucultuldu)

# 4- 'website' icerisinde kac tane a var . count('a')

kacTane = website.count("a")
print(kacTane)

#ya da mesela
degisik = website.count("www",0,10) # www ifadesi 0 ile 10 aralıgında kac tane var.
print(degisik,"*")
# 5- 'website' www ile baslayip com ile bitiyor mu?
bas = website.startswith("www")
son = website.endswith("com")

# 6- 'website içinde '.com' ifadesi var mı?

index = website.find(".com")
index2 = website.index(".com")

index1 = website.find(".com",0,10)
#ayni şekilde find ethodunun da sağdan ve soldan da baslatıp baktırabiliriz.
print(index)
print(index1)
print(index2,"-") #find ile index methodları arasındaki fark şu index bir şey bulamazsa hata dönderir find ise -1 dönderir.


# 7- course icindeki karakterlerin hepsi alfabetic karakterler mi? (isalpha)(isdigit)

alfabmi = course.isalpha()
print(alfabmi)

# 8- 'contents ifadesini satirda 50 karakter icine yerlestirip sağ ve soluna * ekleyiniz.

print("contents".center(50,"*"))

# 9- 'course' karakter dizisindeki tüm boşlukları alıp "-" ile degistirin

tirelendi = course.replace(" ","-")
print(tirelendi)

# 10- Hello World karakter dizisinde World kısmını "There" olarak degistirin

str7 = str.replace("World","There")
print(str7)

# 11- course karakter dizisini bosluk karakterlerinden ayırın 

ayirdim = course.split()
print(ayirdim)