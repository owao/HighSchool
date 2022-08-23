###
# https://www.acmicpc.net/problem/1033
# 완전 탐색: 1033 칵테일 (골드 1)
###

N = int(input())  # 전체 재료 개수 N
for i in range(N-1):  #  재료에 대한 재료비를 줄당 입력
    a,b,p,q = map(int, input().split())
