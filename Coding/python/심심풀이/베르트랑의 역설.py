from random import *
from math import *

a=[1, -1]
r=sqrt(3)
l=0
s=0
k=10
nn=""
asdf=0

for t in range (8):
    for i in range(k):
        x1=uniform(-1,1)
        p=choice(a)
        y1=sqrt(-(x1**2)+1)*p

        x2=uniform(-1,1)
        q=choice(a)
        y2=sqrt(-(x2**2)+1)*q

        len=sqrt((abs(x1-x2))**2+(abs(y1-y2))**2)


        if len>r:
            l=l+1
        else:
            s=s+1
            
    asdf=asdf+1
    if asdf==1:
        nn="열"
    if asdf==2:
        nn="백"
    if asdf==3:
        nn="천"
    if asdf==4:
        nn="만"
    if asdf==5:
        nn="십만"
    if asdf==6:
        nn="백만"
    if asdf==7:
        nn="천만"
    if asdf==8:
        nn="억"
            
    
    print("%s 번 돌렸을 때 현이 더 긴 경우: %d" %(nn, l))
    print("%s 번 돌렸을 때 변이 더 긴 경우: %d" %(nn, s))
    print("%s 번 돌렸을 때 현이 더 긴 통계적 확률: %.1f" %(nn,(l/k)*100))
    print()
    l=0
    s=0
    k=k*10


'''
a=[]
x=-1
y=-1

while x<=1:
    while y<=1:
        if (x*x)+(y*y)==1:
            a.append([x,y])
            y=y+0.001
        else:
            y=y+0.001
    x=x+0.001
    y=-1

print(a)

'''
#반지름이 1인 삼각형의 한 변의 길이=sqrt(3)
