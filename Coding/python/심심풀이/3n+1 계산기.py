k=1
while True:
    n=int(input("자연수를 입력하세요: "))
    while True:
        if n<=0:
            n=int(input("자연수로 입력해주세요: "))
        else:
            break
    
    while n >= 0:
        if n % 2 == 0:
            print(n)
            n=int(n/2)
            k+=1
        else:
            if n==1:
                print(n)
                break
            else:
                print(n)
                n=int(n*3)+1
                k+=1
    print("%d단계를 거쳤습니다." %(k))
    print()
    k=1
