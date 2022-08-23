A=int(input()) #원래 값
a=A #복제 값
c=0 #사이클 값

while True:
    if a<10:
        a=a*11
        c+=1
        if a==A:
            break
        continue
    q=a%10 #1의자리
    p=a//10 #10의자리
    s=q+p #각 자리의 숫자를 더함
    S=s%10 #새로 만든 수의 1의 자리
    a=q*10+S #새로 만든 두자리 수
    c+=1
    if a==A:
        break

print(c)
