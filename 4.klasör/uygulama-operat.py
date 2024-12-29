x,y,z = 2,5,107

numbers = 1,5,7,10,6

# 1-Kullanicidan aldıgınız 2 sayının carpımı ile x,y,z toplamının farkı nedir

# #---- biliyoruz ki input dize haline alır biz onu eğer sayı olarak kullancaksak int diye typecasting yapmamız lazım.

# number1 = int(input("1.sayiyi giriniz"))
# number2 = int(input("2.sayiyi giriniz"))
# toplam = x + y + z
# carpim = number1*number2
# result = carpim - toplam
# 2- - ynin x e kalansız bölümünü hesaplayınız

result = y // x #bolum cevabı vermeli

# 3-(x,y,z) toplamının mod 3 ü nedir?

result = (x + y + z) % 3

# 4- y nin x.kuvvetini hesaplayınız

result= y**x

# 5-x,*y,z = numbers işlemine göre z nin küpü kaçtır

x,*y,z = numbers #x birinci elemani alır.z sonuncu elemani alir ortadaki is egeriye kalan elemanları alır.
result = z**3

# 6- x,*y,z numbers işlemine göre y nin degerleri toplamı kacıtr.?

x,*y,z = numbers
result = y[0] + y[1] + y[2]

print(result)
