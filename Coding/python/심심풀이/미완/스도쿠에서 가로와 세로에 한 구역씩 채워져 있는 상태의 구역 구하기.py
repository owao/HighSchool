A=[1,5,6,8]
B=[1,2,8,9]
C=[2,5,6,9]
D=[1,3,6,7]
E=[1,2,3,4]
F=[2,4,6,7]
G=[3,5,7,8]
H=[3,4,8,9]
I=[4,5,7,9]

Q=[1,2,3,4]

K=[A,B,C,D,E,F,G,H,I]

from random import *

def lenth(K):
    size=[]
    for i in K:
        k=len(i)
        size.append(k)
    size.sort()
    return size[0]

def short(k,K):
    shuffle(K)
    for i in K:
        a=len(i)
        if a==k:
            return i
        else:
            continue

def result(K):
    a=lenth(K)
    b=short(a,K)
    return b
    


for i in E:                     #1234 집합에서부터 시작
    for k in K:                 #전체 집합에서 i 값을 지워버림
        if i not in k:
            continue
        else:
            k.remove(i)
            
    E=[i]                       #1234 집합의 값을 결정
    K.remove(E)                 #결정이 된 집합을 지움
    
    a=result(K)
    b=choice(a)                 #가장 개수가 적은 집합을 랜덤으로 골라 수를 하나 랜덤으로 고름

    for k in K:
        if b not in k:
            continue
        else:
            k.remove(b)         #전체 집합에서 b 값을 지워버림
            
    K.remove(a)                 #결정이 된 집합을 지움


    
