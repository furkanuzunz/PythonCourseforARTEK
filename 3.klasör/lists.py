#bir stringin/karakter dizisinin içindeki her bir karakter aslında bir listenin öğesini temsil ediyor.
#dolayısıyla listeler kavramı da aslında string kavramı gibi algılanabilir.
#Split methodu her bir bosluktan ayırıp bunları ekrana yazdırıyodu.
# message = "Hello There. My name is Furkan Uzun".split()
# print(message)

# myList = [1,2,3]
# myList = ["bir",2,True,5.7]
# print(myList)

# list1 = ["bir","iki","uc"]
# list2 = ["dort","bes","alti"]
# numbers = list1 + list2
# print(numbers)
# print(len(numbers))
# print(numbers[2])

userA = ["Furkan",23]
userB = ["Osman",22]

users = [userA,userB]
users2 = userA + userB
print(users)
print(users[0])
print(users[0][0])
print(users2)
print(users2[0])