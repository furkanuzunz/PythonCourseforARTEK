#tuple () lerle dictionary tipi ise {} lerle kullanılır:

#key - value sistemi kullanılır

# 41 => Kocaeli 34 => İstanbul

#dictionary olmadan bu islemi nasıl yaparız bir bakalım.

sehirler = ["Kocaeli","İstanbul"]
plakalar = [41,34]

plakalar[sehirler.index("Kocaeli")]
plakalar[sehirler.index("İstanbul")]

#----bununla ugrasmak yerine dictionary tipini kullanabiliriz.

# print(plakalar["Kocaeli"]) ifadesinin bizi 41 e götürüyor olmasını istiyoruz.
#key bilgisiyle value bilgisine ulasmak bizim amacimiz

#---- plakalar = {"key" : "value"}

plakalar = {"Kocaeli" : 41, "İstanbul" : 34}

print(plakalar["Kocaeli"])
print(plakalar["İstanbul"])

#mesela şöyle ekleme yapabiliriz.

plakalar["Ankara"] = 6
plakalar["Kocaeli"] = "new value"
print(plakalar)

users = {
    "Furkan uzun" : {
        "age" : 36,
        "roles" : ["user"],
        "email":"fuzun096@gmail.com",
        "phone" : "05453527008"       
    },
    "Kadir Kacar" : {
        "age":22,
        "roles" : [ "admin","user"],
        "email":"dostluk5561@gmail.com",
        "phone":"05657678888"        
    }
}

#iç içe key value mevuzusu yaptık üstte

print(users["Furkan uzun"])  #bu hepsini verir bize
print(users["Furkan uzun"]["age"])  # age bilgisini verir

print(users["Kadir Kacar"]["roles"][0]) #bize admin cıkıtı vermelidir.





