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

while True:    
    a=int(input("구하고자 하는 범위의 첫 숫자를 입력하세요: "))
    b=int(input("구하고자 하는 범위의 마지막 숫자를 입력하세요: "))

    print("%d부터 %d까지의 소수를 출력합니다." %(a,b))
 
    n=int()
    for n in range(a, b+1):
        if prime_number(n) is True:
            print(n)

    c=str(input("끝내시려면 .을 입력해 주십시오. 아니라면 재시작합니다."))
    if c==".":
        break
    else:
        continue
