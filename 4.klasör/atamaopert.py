x,y,z = 5,16,20

print(x,y,z)

x , y = y , x

print(x,y,z)

x = x + 5
x += 5

x *= 5 # x = x *5 aynı şeylerdir c++ daki gibi
x %= 5 #kalan
x // 5   #tam bolme saglar.

y **= 5  #üs alma işareti

print(x,y,z)


values = (1,2,3)

print(values)
print(type(values))

a,b,c = 4,5,6
print(a,b,c)

values_2 = (7,8,9)

a,b,c = values_2
print(a,b,c)

#fazla değer oldugunda bak simdi

values_3 = (1,2,3,4,5,6)

d,e,f = 5,6,7

# d,e,f = values_3 # burada 1=d , 2 = e, ama geri kalanın hepsi direkt f ye gidemez ancak
# #liste yaparsak f yi o zaman gider.
#  ----*---- operatörü unpacking işlemi yapar, belirtilen degiskene kalan
# tüm ögeleri bir liste halinde atar

d,e,*f =values_3
print(d,e,f)
