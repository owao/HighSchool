from random import *

L=[] #전체 리스트
while True:
    k=list(map(int,input().split()))
    if k[0]==0:
        break
    else:
        del k[0]
        L.append(k)
        
for i in L: #앞에 있는 리스트부터 6개씩 뽑는 법을 출력
    k=len(i) #리스트 크기
    for j in range(2**k):
        asdf
    print()


def sw(k): #스위치로 복권 오름차순 출력하기(이진수)
