from math import factorial as f

n,m,o=input().split(' ') #행, 열, 동그라미 칸
N=int(n)
M=int(m)
O=int(o)

a=int(O%N) #행의 줄
b=int((O//N)+1) #열의 줄
#O의 좌표==(a,b+1)

q=f(a+b)/(f(a)*f(b)) #시작 지점에서 동그라미 칸까지 가는 방법
p=f(N-a+M-b)/(f(N-a)*f(M-b)) #동그라미 칸에서 끝까지 가는 방법
print(q)
print(f(a)*f(b))
print(int(q*p))
