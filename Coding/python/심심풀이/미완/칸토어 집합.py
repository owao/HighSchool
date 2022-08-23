def rem(a,b,n): #b는 좌표,n은 지우는 횟수
    c=b+a
    nn=3**n
    for i in range(n):
        t.up()
        t.goto(c,0)
        t.down()
        t.color("white")
        t.fd(a)
        c=c+2*a
        


import turtle as t

n=int(input("몇 단계까지 칸토어 집합을 진행하시겠습니까?"))


t.speed(1)
t.up()
t.goto(-300,0)
t.down()
t.fd(600)

a=600  #길이

for i in range(n):
    a=a/3
    rem(a,-300,n)
    t.up()
    t.goto(0,0)
    
