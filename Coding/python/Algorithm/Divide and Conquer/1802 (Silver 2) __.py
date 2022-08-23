###
# https://www.acmicpc.net/problem/1802
# 분할 정복: 1802 종이 접기 (실버 2)
###

#examine_fold: 접힌 방향 조사 후 가능하면 True, 불가능하면 False 반환
def examine_fold(string):

    return bool


#main code
#N: 테스트 케이스 개수 파악
N=int(input())
caselist=[]

#caselist에 N개의 검증해야할 케이스를 문자열로 저장
for i in range(N):
    case=str(input())
    caselist.append(case)

#caselist 안의 모든 케이스를 examine_fold 함수로 검증
for i in range(N):
    bool = examine_fold(caselist[i])
    if bool == True:
        print("YES")
    elif bool == False:
        print("NO")
