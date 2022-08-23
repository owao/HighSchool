def combination(a,b):
    k=1
    s=1
    for p in range(b):
        k=k*a
        a=a-1
    while b>=1:
        s=s*b
        b=b-1
    w=int(k/s)
    return w

print("파스칼의 삼각형을 나눗셈을 이용해서 시어핀스키 삼각형을 출력합니다.")
a_1=int(input("나눌 숫자를 골라 주세요."))
a_2=int(input("%d를 몇 제곱한 단까지 출력할까요?" %(a_1)))
a=a_1**a_2
b=a_1**a_2
t=5*a
s=0
blackdot=0
whitedot=0

from turtle import *
speed(0)
up()
left(90)
fd(t)
down()

for i in range(a):               #가로
    for k in range(a):           #세로
        if combination(i,k)==0:
            break
        if combination(i,k)%a_1==0:
            dot(10, "white")
            up()
            right(90)
            fd(10)
            left(90)
            down()
            whitedot+=1
        else:
            dot(10, "black")
            up()
            right(90)
            fd(10)
            left(90)
            down()
            blackdot+=1
    up()
    goto(s-5,t-10)
    down()
    t=t-10
    s=s-5

asdf=whitedot/(blackdot+whitedot)
print()
print("전체 원의 개수는 %d 개입니다." %(blackdot+whitedot))
print("검은 원의 개수는 %d 개입니다." %(blackdot))
print("흰 원의 개수는 %d 개입니다." %(whitedot))
print()
print("흰 원의 비율은 %.2f입니다." %(asdf*100))
