# #ogrenciler listemiz var ve her ogrencinin bilgileri olucak.
# #her ogrencinin bi key numarası var onlara ait olan valuelar var


# ogrenciler = {
#     "120": {
#       "ad":"Furkan",
#       "Soyad":"Uzun",
#       "telefon":"545 352 7008"  
#     },
#     "125":{
#         "ad":"Can",
#         "Soyad":"Korkmaz",
#         "Telefon":"532000000"  
#     },
#     "128": {
#         "ad": "vOLKAN",
#         "soyad":"yükselen",
#         "telefon":"532 000 00 93"
#     },
# }

#1-bilgileri verilen öğrencileri kullanıcıdan aldıgınız bilgilerle
#dictionaey içinde saklayınız

#2- öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.



#------------1---------
ogrenciler = {}

key_number = input("ogrenci no: ")
name = input("ogrenci adi: ")
surname = input("ogrenci soyad: ")
phone = input("ogrenci telefon: ")

# ogrenciler[key_number] = {
#         "ad" : name,
#         "soyadi" : surname,
#         "phone" : phone
# } #bu islemi update methoduyla da yapabiliriz.

ogrenciler.update({
        key_number: {
            "ad":name,
            "surname":surname,
            "phone":phone 
        }
}#buradan virgğl diyerek bir object daha ekleyebiliriz.
)

key_number = input("ogrenci no: ")
name = input("ogrenci adi: ")
surname = input("ogrenci soyad: ")
phone = input("ogrenci telefon: ")

ogrenciler.update({
        key_number: {
            "ad":name,
            "surname":surname,
            "phone":phone 
        }
}#buradan virgğl diyerek bir object daha ekleyebiliriz.
)

key_number = input("ogrenci no: ")
name = input("ogrenci adi: ")
surname = input("ogrenci soyad: ")
phone = input("ogrenci telefon: ")

ogrenciler.update({
        key_number: {
            "ad":name,
            "surname":surname,
            "phone":phone 
        }
}#buradan virgğl diyerek bir object daha ekleyebiliriz.
)


#print(ogrenciler)


#--------2---------
print("*"*50)
show_number = input("bilgierini görmek istediğiniz numarayı giriniz")
ogrenci = ogrenciler[show_number]
print(ogrenci)
#print(ogrenciler[show_number])

print(f"aradıgınız {show_number} nolu ogrencinin adi : {ogrenci["ad"]} soyad :{ogrenci["surname"]} ve telefonu ise {ogrenci["phone"]}dir.")


