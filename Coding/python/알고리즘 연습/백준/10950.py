T=int(input()) #test case
A=[]
B=[]

for i in range(T):
    a,b=map(int, input().split())
    A.append(a)
    B.append(b)

for i in range(T):
    q=A[i]
    p=B[i]
    S=q+p
    print(S)
