
# 1- "Bmw,Mercedes,Opel,Mazda"elemanlarına sahip bir liste olusturunuz.

arabalar = ["Bmw","Mercedes","Opel","Mazda"]
print(arabalar)

# 2- Liste kaç elemanlıdır

eleman = len(arabalar)
print(eleman)

# 3-Listenin ilk ve son elemanı nedir

print(arabalar[0])
print(arabalar[eleman-1])   #print(arabalar[-1])  # Listenin son elemanını verir.


# 4- Mazda degerini Toyota ile degisitiriniz

 # arabalar[eleman-1] = "Toyota"
print(arabalar)

# 5-Mercedes listenin elemanı mıdır? 

isThere = "Mercedes" in arabalar
print(isThere)

# 6- Listenin -2 indeksindeki değer nedir?

indeks_2 = arabalar[-2]
print(indeks_2)

#7-Listenin ilk 3 elemanını yazınız

result = arabalar[0:3]
result2 = arabalar[:-1]
print(result)
print(result2)

#8-Listenin son 2 elemanı yerine "Toyota" ve "Renault" degerlerini ekleyiniz

arabalar[-2:] = ["Toyota","Renault"]
print(arabalar)
#9-Listenin üzerine "Audi" ve "Nissan " degerlerini ekleyin

arabalar[eleman:] = ["Audi","Nissan"]
print(arabalar)
# ya da  #
arabalar = arabalar + ["Dacia","Duster"]
print(arabalar)

#10-Listenin son elemanını silin

del arabalar[-1]
print(arabalar)

#11-Liste elemanlarını tersten yazdırın

arabalarNew = arabalar[::-1] # iki noktanın sebebi bütün elemanları secmis oluyoruz.
print(arabalarNew)

#12-Aşağıdaki verileri bir liste halinde saklayınız

    #studentA: Yiğit Bilgi 2010,(70,60,70)
    #studentB: Sena Turan 1999, (80,80,70)
    #studentC: Ahmet Turan 1998,(80,70,90)
    
studentA = ["Yiğit","Bilgi",2010,(70,60,70)]   
studentB = ["Sena","Turan",1999,(80,80,70)]
studentC = ["Ahmet","Turan",1998,(80,70,90)]

print(studentC[3][0])

him = f"{studentA[0]} {studentA[1]} {2024 - studentA[2]} yasinda ve not ortalamsi {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}dir." 
print(him)
students = [studentA,studentB,studentC]   


