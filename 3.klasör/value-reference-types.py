#value types string ve number tipleri gibi
#farklı alanlara tanımlanan veri tipleridir.
x = 5
y = 25

x = y

y = 10

print(x,y)

#----reference types---->>> list gibi class gibi

a = ["apple","banana"]
b = ["apple","banana"]

a = b 
'''
   biz burada a nın icerigini b ye esiledigimiz icin 
   ikisi de artik ayni adresi aldı.
   liste üzerinde yaptıgımzı hernangi bir degisiklik aynı adresleri
   gösterdikleri icin a da da degisecektir.
   ''' 
   #biz listelerde aslında bir adres tasıyoruz.bu adres bilgisinin karsılıgı 
   # value yani degerler bellegin baska kısmında tutuluyor.yani her listenin degeri bi adres aslında o adreslerin karsılıgı da bir value.
    #ben bir liste tuttugumda direkt listenin adreslerini tutuyorum aslında.o listenin adreslerinin icinde de degerler var.
    #yani ben listeA ve listeB yi mesela eşitlediğimde direkt olarak adresler eşitleniyor.
    #ben bu haldeyken bir listede degisiklik yaparsam otomatikmen diğeri de değişecek.
  ## biz listeyi olusturdgumuzda python bir bellek alanı ayırır.ve listenin tüm elemanlarını
  # o adrese , bellek kısmına koyar. listenin kendisi bu bellekteki alana işaret eder.
  # yani pointer gibi bir işlev görür aslıdna. 
  # a degiskeni bellek adresini taşır yanii ona işaret eder.iki listeyi birbirne eşitlediğimizde ikisi de aynı bellek adresine işaret eder.
  #python pointer vb işleleri bizim için otomatikman yapar
"""
yani askında listeler pointer gibi davranır
Evet, tam olarak öyle. Python'da listeler, pointerlar gibi davranırlar çünkü bellek adreslerini tutarlar. Bu adresler, listelerin içerdiği değerlerin bulunduğu bellekteki yeri işaret eder.

Bu nedenle, bir listeyi başka bir listeye atadığınızda, iki liste de aynı bellek adresini paylaşır. Bu durum, listeler üzerinde yapılan değişikliklerin her iki listeyi de etkilemesine neden olur.

Bu, Python'da listelerle çalışma şekli açısından C++'taki pointer kavramına oldukça benzer. Ancak Python, pointerları doğrudan yönetmenize gerek kalmadan bu işlemleri sizin için otomatik olarak yapar,
    """
  
   #reference mevzusu aslında bellek icin bize kolaylık sağlar.kopyaladıgımzıda biz bunlaru yeni bir yer açılmasın
   #aynı yerden devam edebilelim sitiyoruz.kopyaladgımız listeyi tkrar kopya icin bir listede tutmak performans açısından yararsız olucak.
    #kopyalama islemi yaptıgımda adresi kopyalaıp ve o adresteki bilgileri istedigimde ki orijinal değerler elime gelsin
    #reference da adreslerle iş yaparız aynı c++ pointerlar gibi
    
b[0] = "grape"
print(a,b) #biz grapei sadece b üzerinde değişmişitk ama otomatikmen o a üzerinde de değisti NEDEN??



