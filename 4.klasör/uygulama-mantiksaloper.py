# 1- girilen sayinin 0-100 araliginda olup olmadigini kontrol ediniz

# a = int(input("sayi giriniz:"))
# result = (a >0 and a <=  100)
# print(f"sayinin aralık kontrolunden cıkan durumu: {result}")


# 2-
#     kullanicidan 2 vize (%60) ve final (%40) notunu alıp ortalama hesapla
#     eger ortalama 50 ve ustundeyse gecti degilse kaldi yazdiriniz
#     a-) ortalama 50 olsa bile final notu en az 50 olmaldiri
#     b-) finalden 70 alindiginda ortalamanın önemi olmasin.

vize1 = float(input("vize 1: "))
vize2 = float(input("vize 1: "))
final = float(input("final: "))

ortalama = ((vize1+vize2)/2)*0.6 + (final * 0.4)
result = ((ortalama > 50) and (final > 50)) or (final >= 70)

print(f"ogrencinin ortalamasi: {ortalama} ve gecme durumu : {result}")