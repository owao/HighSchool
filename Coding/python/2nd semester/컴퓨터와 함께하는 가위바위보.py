import random
p=0
c=0

while True:
    player=input("가위, 바위, 보? ")
    print()
    computer=random.choice(['가위', '바위', '보'])
    print("선수:" , player, "vs", "컴퓨터:",computer)
    print()

    if player=="가위" and computer=="보":
        print("선수 승!")
        p=p+1
    if player=="보" and computer=="바위":
        print("선수 승!")
        p=p+1
    if player=="바위" and computer=="가위":
        print("선수 승!")
        p=p+1

    if player=="보" and computer=="가위":
        print("컴퓨터 승!")
        c=c+1
    if player=="바위" and computer=="보":
        print("컴퓨터 승!")
        c=c+1
    if player=="가위" and computer=="바위":
        print("컴퓨터 승!")
        c=c+1

    if player==computer:
        print("무승부!")

    print()
    print("선수 %d점 : 컴퓨터 %d점" %(p,c))
    print()
    print()

    if p==10:
        print("선수가 이겼습니다!")
        break
    else:
        if c==10:
            print("컴퓨터가 이겼습니다!")
            break
        else:
            continue
        
