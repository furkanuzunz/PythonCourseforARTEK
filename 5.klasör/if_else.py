if 3>2:
    print("hoş geldiniz")
#true ise çalışır.ifin yanına yazdıgımız koşulun bir true ya da false üretmesi gerekir.
print("*"*50)

isloggedin = True
if isloggedin:
    print("ula ne edeysun")
    
print("*"*50)
username = "sadikturan"
password = "1234"

isThat = (username == "sadikturan") and (password == "1234")
if isThat:
    print("giriş başarili")
else:
    print("username ya da parola yanlis")

print("*"*50)