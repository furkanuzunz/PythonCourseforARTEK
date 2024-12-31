#global scope
x = "global x"

def function():
    #local scope
    x = "local x"
    print(x)
    
function()
print(x)

#fonksiyonlar yeni bir tanımlama alanı kullanır.
#diyelim ki fonksiyon icinde x e dair bir local değişken yok o zaman fonksiyonun icindeki print(x) ifadesi
# global kapsamdkai x in karşılığını yazdirir.

#global
name = "furkan"
print(name)

def change_name(new_name):
    #local
    name = new_name
    print(name)
    
change_name("osman")
print(name)

# ikisi de aynı degislken isimleri ama nerede tanimlandigi ve yazdiridliği çok önemli

name = "global string"

def greeting():
    name = "Furkan"
    
    def hello():
        print("hello " +  name)#buradaki fonksiyon icin name hemen üsttekidir.hello fonksiyonu icin 
        #global degisken buradakidir hemen üsttekidir.
        #eğer burada name diye bir degisken tanimlamasaydik o zaman ondanda üstteki olan name degiskenini kullanirdi.,
    
    #greeting fonksiyonu kapsamı icerisinde hello() fonksiyonunu cagırıyoruz.
    hello()
#sonra da en dişarida greetingi cagiricaz.
greeting()

print(name) #mesela burada "global string" aliriz cikti.


#------ #####

x = 50
def test(x):
    print(f"x : {x}")
    
    x = 100
    print(f"changed x to: {x}")
    
test(x)#burada x = 50 yi göndderdik. o x degisti artik ve 100 oldu ama icerideki x te oldu.
print(x) #burada ise hala 50

#eğer dişarida tanimladiğimiz degiskeni fonksiyonun icinde değiştrmek sitiyosak 
#fonksiyon icinde ----- global x ---- şeklinde yapmaliyiz.
def test():
    global x
    print(f"x : {x}")
    
    x = 100
    print(f"changed x to: {x}")
    
test()
print(x) #100 verir artik iceride degistik cunku