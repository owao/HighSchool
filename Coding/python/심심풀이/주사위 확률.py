from random import *

a=[1,2,3,4,5,6]
k=0
s=10
one=0
two=0
three=0
four=0
five=0
six=0
nn=""
asdf=0

for t in range (8):
    for i in range(s):
        k=choice(a)
        if k==1:
            one=one+1
        if k==2:
            two=two+1
        if k==3:
            three=three+1
        if k==4:
            four=four+1
        if k==5:
            five=five+1
        if k==6:
            six=six+1
            
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
        
    print("%s번 돌렸을 때 1이 나올 경우의 수: %d" %(nn,one))
    print("%s번 돌렸을 때 2가 나올 경우의 수: %d" %(nn,two))
    print("%s번 돌렸을 때 3이 나올 경우의 수: %d" %(nn,three))
    print("%s번 돌렸을 때 4가 나올 경우의 수: %d" %(nn,four))
    print("%s번 돌렸을 때 5가 나올 경우의 수: %d" %(nn,five))
    print("%s번 돌렸을 때 6이 나올 경우의 수: %d" %(nn,six))
    print()
    print("%s번 돌렸을 때 1이 나올 확률: %.2f" %(nn,one/s*100))
    print()
    print()
    
    one=0
    two=0
    three=0
    four=0
    five=0
    six=0
    s=s*10

#돌리는 횟수가 커질수록 주사위 눈이 나오는 수학적 확률인 1/6(16.66%)에 점점 가까워지는것을 볼 수 있다.
#그리고 횟수가 커질수록 주사위 눈이 나오는 경우의 수가 16xxxx정도로 점점 비슷해져서, 주사위 눈이 나올 확률은 전부 균일하다는 것을 알 수 있다.
