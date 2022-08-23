def asdf(n):
    if n<=100:
        return 6
    if n<=10000:
        return 14
    if n<=1000000:
        return 21
    if n<=100000000:
        return 27
    else:
        return n/10000000
    
while True:
    a=int(input("숫자를 입력하세요: "))
    b=int(asdf(a))

    print()
    print("%d은(는)" %(a), end=" ")

    while a>0:
        while b>=0:
            if a-(2**b)>=0:
                print(2**b, end=" ")
                a=a-(2**b)
            b-=1            
    print("로 이루어진 숫자입니다.")

    print()
    pot=str(input("계속하시려면 YES를, 아니라면 아무 키나 입력해주세요."))
    if pot=="YES":
        print()
        continue
    else:
        break
