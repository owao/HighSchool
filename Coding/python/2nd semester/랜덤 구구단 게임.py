print("10초 안으로 답을 맞춰야 하는 20x20의 구구단 게임입니다.")
s=str(input("게임을 시작하시겠습니까?"))

if s=="NO":
    exit()

while True:
    import random
    import time
    a=random.randint(1,20)
    b=random.randint(1,20)
    st=time.time()

    c=int(input("%d X %d = " %(a,b)))
    en=time.time()
    
    if abs(st-en) <= 10:
        if c==a*b:
            print(" --> BINGO")
        else:
            print(" --> Oops!!, correct answer is", a*b)
            print()
            asdf=str(input("게임을 계속하시겠습니까?"))
            if asdf=="YES":
                continue
            else:
                break
    else:
        print(" --> Oops!!, you are late!")
        print()
        asdf=str(input("게임을 계속하시겠습니까?"))
        if asdf=="YES":
            continue
        else:
            break
