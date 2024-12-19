message = "Hello there. My name is Furkan Uzun"
print(message)

message1 = message.upper() #harfler buyur
print(message1)

message2 = message.lower() #harfler kculur
print(message2)

message3 = message.title()  #bas harfler büyükolur
print(message3)

message4 = message.capitalize()  # sadece ilk harf buyur
print(message4)

 ##diyelim basta bir bosluk karakteri var. bunu gidermek icin strip methodunu kullanırız.
message20 = " Hello there.My name is furkan"
message21 = message.strip()
print(message21)

#eğer split methodunu kullanırsak verilen string ayrı ayrı dizilere bölünerek bize verilir.Bosluk karakterlerinden itibaren ayrılır.
#['Hello', 'there.my', 'name', 'is', 'furkan'] seklinde cıktı alırız.
message5 = message.split()
print(message5)
print(message5[0]) #hello cıktısını alırsın

#eğer kendi istediğin bir yerden itibaren ayrılmasını istersen parametre olarak vermen gerekir.
#cıktısı ['Hello there', ' My name is Furkan'] olur.
message6 = message.split(".")
print(message6)

## splitle ayırdık diyelim ben bunları sonrasında birleştirmek istersem de birleştirikren araya ne girmesini istersek onu yazıyoruz yani şu şekilde aslında
# ' '.join(message) gibi.      istersek yıldız da ekleyebilrizii.
message7 = "*".join(message5) # message5 split edilmis hali cumlenin
print(message5)
print(message7)

#find methodu cumlede aramak sitedigimiz kelime varsa bize bir numara döndürür.
#Buldugu kelimenin ilk harfinin indeks numarasnı geri döndürür bize. kelime yoksa da -1 gönderir.
index = message.find("Furkan")
print(index)

#startswith methodunu biz hangi harfle basladıgını bulmak icin kullanabiliriz.
isFound = message.startswith("H")
print(isFound) #true ya da false verir.
#endswith
isFound2 = message.endswith("n")
print(isFound2)

#replace methodu ilk parametreyi cumlede arar 2.parametre ile de degisir.
message8 = message.replace("Furkan","Eda")
print(message8) 
message9 = message.replace("M","n").replace("F","H")
print(message9)

#center methodu belirli bir alan belirleriz oranın tam ortasına cumlemizi yerlestirir. sağ ve soldan eşit boşluklar bırakılıyor ve tam ortalanıyor
message10 = message.center(74)
message11 = message.center(50,"*") ## sağdan ve soldan eşit bir şekilde *
print(message10)
print(message11)