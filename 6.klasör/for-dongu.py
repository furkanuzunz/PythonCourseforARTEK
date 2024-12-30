numbers = [1,2,3,4,5]

#forun yaptıgı burada numbers listesindeki her elemanı num icerisine at
#ve her seferinde geleni yazdırır.

#yani önemli olan aslında listenin eleman sayisi kadar for döngüsü dönüyor olması
#cunku mesela ben print(helllo) desem 5 defa hello olacak
for num in numbers:
    print(num)
    

names = ["Çinar","Sadik","Furkan"]

for name in names:
    print(f"My name is {name}")
    
#ya da----
name = "Furkan Uzun" #stringde bir liste gibi akrakter dizesidir.
#ve her bir eleman bir dizi elemanı gibi degerlendiriliyor.
#burada string ifadenin her bir karakteri yazdirilir.
for n in name:
    print(n)

tuple = (1,2,3,4,5)

for t in tuple:
    print(t)
    
my_tuple = [(1,2),(1,3),(3,5),(5,7)]

for z in my_tuple:
    print(z)

my_tuple = [(1,2),(1,3),(3,5),(5,7)]

for a,b in my_tuple:
    print(a,b)

#dictionary tipinde sadece key bilgilerini yazdirir.Value bilgilrerini yazdirmaz.

dic = {"k1":1, "k2":2, "k3":3}

for item in dic:
    print(item) 

#eğer valuelara ulasmak istiyorsak şu şekilde:

for item2 in dic.items():
    print(item2)

# dic.items() Nedir?: items() metodu, bir dictionary nesnesinin anahtar-değer çiftlerini döndürür. Bu dönüş, "dict_items" 
# olarak adlandırılan özel bir nesne türüdür.

# dict_items Nesnesi: items() metodu, dict_items türünde bir nesne döner. Bu nesne, sözlükteki 
# tüm anahtar-değer çiftlerini içeren bir koleksiyondur.

# Nesneye Erişim: Python'da bir sözlüğe erişmek için . operatörü kullanılır. Bu, sözlüğün (ya da başka herhangi bir nesnenin) 
# metotlarına ve özelliklerine erişmenizi sağlar. items() metodu, bu nesne metodlarından biridir.

for key,value in dic.items():
    print(key,value)