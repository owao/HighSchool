#유클리드 호제법 사용

while True:
    a=int(input("숫자를 입력하세요: "))
    
    print()
    print("%d은(는)" %(a))

    b=0

    while a>0:
        if a==1:
            print(2**b)
            break
        if a%2==1:
            print(2**b)
            a=(a-1)/2
            b+=1
        if a%2==0:
            a=a/2
            b+=1
            continue
    print("로 이루어진 숫자입니다.")

    print()
    pot=str(input("계속하시려면 YES를, 아니라면 아무 키나 입력해주세요."))
    if pot=="YES":
        print()
        continue
    else:
        break
