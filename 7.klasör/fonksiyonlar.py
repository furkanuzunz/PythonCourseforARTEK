def sayHello():
    print("hello")
    
sayHello()    
sayHello() 

def sayHello2(name):
    print("hello " + name)   

sayHello2("Furkan")

def sayHello3(name):
    return "hello " + name

message = sayHello3("usmanim")
print(message)
 

def total(num1,num2):
    return num1 + num2

toplam = total(2,4)
print(toplam)


def yasHesapla(dogumYili):
    return 2024 - dogumYili
ageFurkan = yasHesapla(2002)
print(ageFurkan)

def EmekliligeKacYilKaldi(dogumYili, isim):
    '''
    DOCSTRıNG : Dogum yiliniza göre emekliliğinize göre kac yil kaldı
    INPUT: DOgum Yili
    OUTPUT: Hesaplanan Yil bilgisi 
    '''
    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas
    
    if emeklilik > 0:
        print(f"emeklilginize {emeklilik}' yil kaldı")
    else:
        print("zaten emekli oldunuz")
        
EmekliligeKacYilKaldi(2002,"Furkan")

print(help(EmekliligeKacYilKaldi))

list = [1,2,3]

print(help(list.append))