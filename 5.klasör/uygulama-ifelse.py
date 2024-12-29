# 1-Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre 
# araligina karsılık gelen not bilgisini giriniz
# 0-24 = 0
# 25-44 = 1
# 45-54 = 2
# 55-69= 3
# 70-84 = 4
# 85-100 = 5

yaz1 = int(input("yazili 1:"))
yaz2 = int(input("yazili 2:"))
sozlu1 = int(input("sozlu 1:"))

ortalama = (yaz1 + yaz2+sozlu1) / 3
if 0<ortalama<24:
    print(f"ortalamaniz: {ortalama} ve notunuz: 0")
elif 25<ortalama<44:
    print(f"ortalamaniz: {ortalama} ve notunuz: 1")
elif 45<ortalama<54:
    print(f"ortalamaniz: {ortalama} ve notunuz: 2")
elif 55<ortalama<69:
    print(f"ortalamaniz: {ortalama} ve notunuz: 3")
elif 70<ortalama<84:
    print(f"ortalamaniz: {ortalama} ve notunuz: 4")
else:
    print(f"ortalamaniz: {ortalama} ve notunuz: 5")

# 2-trafiğe cıkıs tarihi alinan bir aracın servis zamanını aşağıdak
# bilgilere göre hesaplayınız.
# 1.bakım = 1.yıl
# 2.bakım = 2.yıl
# 3.bakim = 3.yıl
# ** süre hesabını alınan gün,ay,yıl bilgisine göre gün bazlı hesaplayınız
# *** dateTtime modülünü kullanmanız gerekiyor.
# (simdi) - (2018/8/1) => gün


# days = int(input("araciniz kac gundur trafikte :"))

# if days<=365:
#     print("1.servis araliği")
# elif 365<days<=365*2:
#     print("2.servis araliği")
# elif 365*2<days<=365*3:
#     print("3.servis araliği")
# else:
#     print("hTALİ SÜRE BİLGİSİ") 

#---datetime modülü ile yapalım
import datetime
#tarihler üzerinde işlemler yapabilmek icin tarihleri datetime objesine dönüştürmemiz gerekir.

tarih = input("araciniz kac gundur trafikte (2018/8/9) :")
tarih = tarih.split("/")
#biz simdiki zamandan bu girilen zamanı cıkartmamız icin alttaki now gibi bi obje tanım
#lamamız gerekiyo cunku hani böyle ayrı ayrı sekilde
trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
now = datetime.datetime.now()
#suan bu ikisi cıkarılabilecek duruma geldi.

fark = now - trafigeCikis
days = fark.days
# print(fark.days) #biz bundan gün bilgiisni alabiliriz.

if days<=365:
    print("1.servis araliği")
elif 365<days<=365*2:
    print("2.servis araliği")
elif 365*2<days<=365*3:
    print("3.servis araliği")
else:
    print("hTALİ SÜRE BİLGİSİ") 

