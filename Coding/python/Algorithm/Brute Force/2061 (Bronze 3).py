###
# https://www.acmicpc.net/problem/2061
# 완전 탐색: 2061 좋은 암호 (브론즈 3)
###

# K: 검증할 키값, L: 인수분해할 확인값, B: 나눠졌는지 확인
K, L = map(int, input().split())
B = True

# L-1까지의 숫자들만 탐색 -> 인수분해되면 B = False 반환 후 탐색 종료
for i in range(L-2):
    if K%(i+2) == 0:
        B = False
        break

#출력
if B == False:
    print("BAD %d"%(i+2))
elif B == True:
    print("GOOD")
