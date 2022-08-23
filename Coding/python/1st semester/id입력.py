a=input("아이디를 입력하세요 : ")
if a=="user" :
    b=input("비밀번호를 입력하세요 : ")
    if b=="1234" :
        print("Welcome")
    else :
        print("Incorrect password")
else :
    print("Incorrect ID")
    print("Try again")
