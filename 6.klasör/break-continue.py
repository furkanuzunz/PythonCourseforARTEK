name = "Furkan Uzun"

for letter in name:
    if letter == "a":
        break
    print(letter)
#break gördüğünde durur ve d,ğer harfler ekrana yazdirilmaz.
print("*"*50)
for letter in name:
    if letter == "a":
        continue
    print(letter)
#mesela continue da ise a harfi görüldüğünde o döngü pas gecilir o harf yazilmadan devam eder.

x = 0
while x < 5:
    x += 1
    if x == 2:
        continue
    print(x)
#2 yi görünce döngüyü pas geccek arttircak devamm etcek. ama x+=1 ifadesi altta olsaydi isler degisirdi.

# 1 den 100 e kadar tek sayilarin toplami

x = 0
result = 0

while x <= 100:
    x += 1
    if(x % 2==0):
        continue
    result += x
print(result)