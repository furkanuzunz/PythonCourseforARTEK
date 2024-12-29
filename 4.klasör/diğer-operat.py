# #ıdentity operator : is

# x = y = [1,2,3] #aynı adres içerisinde tanımlanmış bir liste

# z =  [1,2,3]

# print(x == y) # true degeirni alırız.
# print(x == z) # sadece degerleir karsilastirdigi icin true alırız

# #mesela biz deger karsilastirmasi değil de referans tipindeki bir verinin adres karsılastırmasında 
# # is operatorunu kullaniriz.
# print(x is y)  # true alırız cunku adresleri esit
# print(x is z)  # false aliriz cunku adresleri esit değil aynı degerler olsa bile.
#  #is ile bildigin hani objeler tamamiyle aynı mı degil mi ona bakıyoruz.
 
# membership operator: in

a = ["apple","banana"]
print("banana" in a) #true gelir
print("banana" not in a) #banana yok mu icinde diyoz var oldugu icin false dönderir