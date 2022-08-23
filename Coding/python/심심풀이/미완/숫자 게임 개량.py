def re(n):
    while True:
        if n==0 or n == 1:
            return n
        else:
            n=int(input("0이나 1만 입력하세요. "))

while True:
    rg=int(input("범위가 될 자연수를 입력해주세요. "))
    print()
    print("1~%d 사이의 숫자를 하나 떠올려 보세요." %(rg))
    print("지금부터 당신이 생각한 숫자를 맞춰 보겠습니다.")
    print()

    
    sen=0
    sum=0
    while 2**sen<rg+1:
        for x in range(2**sen,rg+1,2**(sen+1)):
            for s in range(2**sen):
                if x>rg:
                    break
                print("%4d"%(x), end=" ")
                x=x+1
            x=x+sen
        print()
        print()
        a=int(input("방금의 숫자들 중 생각한 숫자가 있으면 1, 없으면 0을 눌러주세요. "))
        a = re(a)
        if a==1:
            a=2**sen
        if a==0:
            a=0
        sum=sum+a
        sen+=1
        print()

    print()
    print("당신이 생각한 숫자는 %d입니다."%(sum))
    print()
    asdf=str(input("다시 하시려면 YES를, 다시 하지 않으신다면 YES를 제외한 아무 키나 입력해주세요. "))
    if asdf == "YES":
        print()
        print()
        continue
    else:
        break
