def re(n):
    while True:
        if n==0 or n == 1:
            return n
        else:
            n=int(input("0이나 1만 입력하세요. "))

while True:
    print("1~60 사이의 숫자를 하나 떠올려 보세요.")
    print("지금부터 당신이 생각한 숫자를 맞춰 보겠습니다.")
    print()

    for x in range(1,60,12):
        for y in range(1,7):
            print("%4d"%(x), end=" ")
            x=x+2
        print()

    print()
    a=int(input("방금의 숫자들 중 생각한 숫자가 있으면 1, 없으면 0을 눌러주세요. "))
    a = re(a)
    if a==1:
        a=1
    if a==0:
        a=0

    print()
    for x in range(2,60,12):
        for y in range(1,4):
            for s in range(2):
                print("%4d"%(x), end=" ")
                x=x+1
            x=x+2
        print()

    print()
    b=int(input("방금의 숫자들 중 생각한 숫자가 있으면 1, 없으면 0을 눌러주세요. "))
    b = re(b)
    if b==1:
        b=2
    if b==0:
        b=0

    print()
    for x in range(4,60,16):
        for y in range(1,3):
            for s in range(4):
                if x>60:
                    break
                print("%4d"%(x), end=" ")
                x=x+1
            x=x+4
        print()

    print()
    c=int(input("방금의 숫자들 중 생각한 숫자가 있으면 1, 없으면 0을 눌러주세요. "))
    c = re(c)
    if c==1:
        c=4
    if c==0:
        c=0

    print()
    for x in range(8,60,16):
        for s in range(8):
            if x>60:
                break
            print("%4d"%(x), end=" ")
            x=x+1
        print()

    print()
    d=int(input("방금의 숫자들 중 생각한 숫자가 있으면 1, 없으면 0을 눌러주세요. "))
    d = re(d)
    if d==1:
        d=8
    if d==0:
        d=0

    print()
    for x in range(16,60,32):
        for y in range(2):
            for s in range(8):
                if x>60:
                    break
                print("%4d"%(x), end=" ")
                x=x+1
            print()

    print()
    e=int(input("방금의 숫자들 중 생각한 숫자가 있으면 1, 없으면 0을 눌러주세요. "))
    e = re(e)
    if e==1:
        e=16
    if e==0:
        e=0

    print()
    for x in range(32,61,6):
        for s in range(6):
            if x>60:
                break
            print("%4d"%(x), end=" ")
            x=x+1
        print()

    print()
    f=int(input("방금의 숫자들 중 생각한 숫자가 있으면 1, 없으면 0을 눌러주세요. "))
    f = re(f)
    if f==1:
        f=32
    if f==0:
        f=0
        
    print()
    print("당신이 생각한 숫자는 %d입니다."%(a+b+c+d+e+f))
    print()
    asdf=str(input("다시 하시려면 YES를, 다시 하지 않으신다면 YES를 제외한 아무 키나 입력해주세요. "))
    if asdf == "YES":
        print()
        print()
        continue
    else:
        break
