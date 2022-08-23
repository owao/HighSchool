###
# https://www.acmicpc.net/problem/6971
# 완전 탐색: 6971 Nasty Numbers (실버 5)
###

#pairs: 인수를 찾고, 인수쌍 중 작은 쪽을 리스트로 저장
def pairs(number):
    num = int(number/2)
    list = []
    for i in range(num):
        a = number%(i+1)
        if a == 0:
            list.append(i+1)
    return list

#nasty: 이중 for문으로 nasty 조건에 맞는 모든 경우의 수 비교
def nasty(number):
    numL = pairs(number)
    for i in range(len(numL)):
        for j in range(len(numL)):
            a=numL[i] + (number/numL[i])
            b=(number/numL[j]) - numL[j]
            if a==b:
                return True
    return False


#main code
#N: 받을 값 개수 파악
N=int(input())
numlist=[]

#numlist에 N개의 검증해야할 값 저장
for i in range(N):
    number=int(input())
    numlist.append(number)

#numlist 안의 모든 값을 nasty 함수로 검증
for i in range(N):
    bool = nasty(numlist[i])
    if bool == True:
        print("%d is nasty"%(numlist[i]))
    elif bool == False:
        print("%d is not nasty"%(numlist[i]))

