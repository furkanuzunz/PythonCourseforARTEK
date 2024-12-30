# range(), enumerate(), zip()

#----------range()--------- 
# ile içine yazdigimiz degere kadar sayi veri bize sıfırdan baslar
for item in range(10):
    print(item)
#yani aslinda bizim icin bir liste olustuyor.

print("\n")

for item in range(2,10):
    print(item)
    
print("\n")

#artis miktarini da 3.parametre ile belirleyebilriiz dostum
for item in range(50,100,10): #10 ar 10 ar 50 den 100 e artacak
    print(item)    

#list methodu kullanarak range ile gelenleri list tipine dönusturmek.
print(list(range(50,100,10)))

print("*"*50)

#-------enumerate---------
# greeting = "Hello There"
# index = 0
# for letter in greeting:
#     print(f"index: {index}, letter: {letter}")
#     index+=1
#bunları böyle ugrasmaktansa direkt enumerate methodu ile halledebiliriz.

greeting = "hello there"

for item in enumerate(greeting):
    print(item)
    
    
print("*"*50)

#--------zip()---------

list1 = [1,2,3,4,5]
list2 = ["a","b","c","d","d"]
list3 = [100,200,300,400,500]
 
 #diyelim ki biz mesela sıfıırncı indeks 1 e birinci indeks olan "b" 2 ye gibi br şey ,s,tyoruz.
#o zaman zip() methodunu kullaniriz. 

eslesilmisHal = zip(list1,list2,list3)
listelenmisHal = list(eslesilmisHal)
print(listelenmisHal)

for item in zip(list1,list2,list3):
    print(item)

for a,b,c in zip(list1,list2,list3):
    print(a,b)
    