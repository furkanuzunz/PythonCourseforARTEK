x = 6

# result = 5 < x <10

# print(result)

#and

result = (x > 5) and (x < 10) #cevap truedir.
        #true  and true => true
        #true  and false => false


#or

result = (x > 0) or (x % 2 == 0) ## ikisinden biri dogruysa true döndürür ikisi de false sa zaten false dönderir.


#not

result = not(x > 0) # x sıfırdan büyükse diye sorduk ama not operatoru tam tersine cevirir true ise false yapar. 


print(result)