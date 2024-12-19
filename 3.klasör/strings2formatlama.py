#stringleri düzenlemek icin bazı methodlarımız vardır

name   = "Furkan"
surname = "Uzun"
age = 22

print("My name is {} {}".format(name,surname))  #format() fonksiyonu, metin içinde yer tutucuları (placeholder) kullanarak, her bir yerine bir değeri yerleştirir

print("My name is {0} {1}".format(name,surname)) #indeks mantıgı da kullanabiliriz. eğer indeksleri degisirsek yazılar da ters olur
print("My name is {1} {0}".format(name,surname)) #uzun furkan cıkar

print("My name is {s} {n}".format(n = name,s = surname)) # bu sekilde de olabilir.

print("My name is {s} {n} and I am {a} years old".format(n = name,s = surname,a = age))

print("My name is {} {} and I am {} years old".format(name,surname,age))

result = 200 / 700
print("the result is {}".format(result))
print("the result is {r:1.3}".format(r = result)) # ondalıklı kısımdan önce 1 kısmı sonra da 3 haneyi yazar.

#fstring metodunu ogrenelim.
#bize asagıdaki kolaylıgı sağlar.
print(f"My name is {name} {surname} and I am {age} years old")

