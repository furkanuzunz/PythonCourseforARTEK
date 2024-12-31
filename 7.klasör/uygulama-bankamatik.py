#bankamatik uygulamasi

sadikHesap = {
    "ad" : "Sadik Turan",
    "hesapNo" : "13245678",
    "bakiye" : 3000,
    "ekHesap": 2000
}

aliHesap = {
    "ad" : "Ali Turan",
    "hesapNo" : "12345678",
    "bakiye" : 2000,
    "ekHesap": 1000
}

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap["ad"]}")
# Python'da bir fonksiyona bir sözlük (dictionary) argüman olarak geçtiğimizde, o sözlüğü fonksiyon içinde farklı bir isimle kullanabiliriz. Örneğin, sadikHesap sözlüğünü paraCek fonksiyonuna argüman olarak geçerken 
# fonksiyon içinde hesap adını kullanabilirsiniz. Bu, fonksiyonun parametre adıdır ve fonksiyonun içinde sözlüğe erişim sağlar.
    if(hesap["bakiye"] >= miktar):
        hesap["bakiye"] = hesap["bakiye"] - miktar
        print("paranizi alabilirsiniz")
        bakiyeSorgula(hesap)
    else:
        toplam =  hesap["bakiye"] + hesap["ekHesap"]
        
        if toplam >= miktar:
            ekHesapKullanimi =input("ek hesap kullanilsin mi : (e/h)")
             
            if ekHesapKullanimi == "e":
                bakiye = hesap["bakiye"]
                ekHesapKullanilacakMiktar = miktar - bakiye
                bakiye = 0
                hesap["ekHesap"] = hesap["ekHesap"] - ekHesapKullanilacakMiktar
                print("paranizi alabilirsiniz.")
                print("paranizi alabilirsiniz")
            else:
                print(f"{hesap["hesapNo"]} nolu hesabınızda {hesap["bakiye"]} bulunmaktadir.")
        else:
            print("uzgunuz bakiye yetersiz")


#simdi söyle bizim disarida tanimadigimiz sadikHesap gibi dictionary veri yapısı aslında reference
#tipinde yapılardır. yani ben bunbları bir methoda bir fonksiyona gönderdigimde bunların adreslerini göndermis olurum
#yani bu da demek oluyor ki ben fonksiyonda bir degisiklik yaptiğimda cikartma ekleme felan iste bu adresle geldiği icn adresin icindeki degeri de gunceelleyecektir.
#reference mevzusunun olayı budur.
#biz aslında nesne gönderdik obje gönderdik yani


#dk 13 önemli

# Hocanızın "obje" veya "nesne" derken kastettiği şey, sözlüklerin (dictionaries) aslında birer nesne olduğudur. Python'da her şey bir nesnedir ve bu nesneler referans (adres) yoluyla taşınır.

# Açıklamak gerekirse:

# Sözlükler (Dictionaries) ve Nesneler: Python'da bir sözlük tanımladığınızda, bu sözlük bir nesne olarak bellekte bir yer kaplar. Bu nesne, sadikHesap veya aliHesap isimleriyle erişilebilir olur.

# Referans Tipleri: Python'da sözlükler ve diğer karmaşık veri tipleri (listeler, sınıflar vb.) referans tipleridir. Bu, onları bir fonksiyona argüman olarak geçtiğinizde, fonksiyona aslında bu nesnenin adresini (referansını) geçirdiğiniz anlamına gelir. 
# Bu da demek oluyor ki, fonksiyon içinde yapılan değişiklikler doğrudan orijinal nesne üzerinde yapılır.

'''
Açıklamak gerekirse:

Sözlükler (Dictionaries) ve Nesneler: Python'da bir sözlük tanımladığınızda, bu sözlük bir nesne olarak bellekte bir yer kaplar. Bu nesne, sadikHesap veya aliHesap isimleriyle erişilebilir olur.

Referans Tipleri: Python'da sözlükler ve diğer karmaşık veri tipleri (listeler, sınıflar vb.) referans tipleridir. Bu, onları bir fonksiyona argüman olarak geçtiğinizde,
fonksiyona aslında bu nesnenin adresini (referansını) geçirdiğiniz anlamına gelir. Bu da demek oluyor ki, fonksiyon içinde yapılan değişiklikler doğrudan orijinal nesne üzerinde yapılır.
'''

'''
Bu kodda:

sadikHesap nesnesi paraCek fonksiyonuna referans (adres) olarak geçer.

Fonksiyon içinde hesap adıyla erişilir ve değişiklikler yapılır.

paraCek fonksiyonundan sonra, sadikHesap sözlüğündeki değişiklikler kalıcıdır ve dışarıdaki sadikHesap nesnesi de güncellenir.

Sonuç olarak, Python'da nesneler fonksiyonlara referans olarak geçirilir ve fonksiyonlar bu nesneler üzerinde doğrudan değişiklik yapabilir. 
Hocanızın bahsettiği "obje" bu anlamda kullanılmıştır.

'''

def bakiyeSorgula(hesap):
    print(f"{hesap["hesapNo"]} nolu hesabınızda {hesap["bakiye"]} tl bulunmaktadir ek hesap limitiniz ise {hesap["ekHesap"]} tl bulunmaktadir")
    
paraCek(sadikHesap,3000)
bakiyeSorgula(sadikHesap)
print("**********************")
paraCek(sadikHesap,2000)
bakiyeSorgula(sadikHesap)
