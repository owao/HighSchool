def prime_number(n):
    if n == 2:
        return True
    if n < 2:
        return False
    if n % 2 == 0:
        return False
    ps = round(n**0.5) +1
    for ps in range(3, ps, 2):
        if n% ps == 0:
            return False
    else:
        return True

A=int()
B=int()

print("짝수를 골드바흐 추측 방식의 소수쌍으로 나타내는 프로그램입니다.")
while True:
    print()
    number=int(input("짝수를 입력해주세요: "))
    while True:
        if number<=0:
            print()
            number=int(input("음수는 짝수가 아닙니다. 다시 입력해주세요. "))
        if number==0 :
            print()
            number=int(input("0은 짝수가 아닙니다. 다시 입력해주세요. "))
        if number%2 ==0 :
            break
        else:
            print()
            number=int(input("짝수로 다시 입력해주세요: "))
    
    f=int(number/2+1)
    sum=0

    if number == 2:
        print()
        print("그 자체로 소수입니다.")
    else:
        print()
        print("%d은 다음과 같은 순서쌍의 합으로 나타낼 수 있습니다" %(number))
        print()
        for A in range(2, f):
            for B in range(2, number):
                if prime_number(A) is True:
                    if prime_number(B)is True:
                        if A+B==number:
                            print("(%d, %d)" %(A,B))
                            sum=sum+1
        print()
        print("총 %d개의 순서쌍이 있습니다." %(sum))
        print("순서쌍은 반대로 해도 동일합니다.")
    print()
    g=str(input("다시 하시려면 YES를, 다시 하지 않으신다면 YES를 제외한 아무 키나 입력해주세요. "))
    if g == "YES":
        continue
    else:
        break
