m,n,h=input().split(' ') #가로, 세로, 높이
M=int(m)
N=int(n)
H=int(h)
box=[] #리스트 속 리스트

for i in range(H): #높이만큼 판을 쌓는다(참조: box[0]이 제일 아래)
    box.append([]) #하나의 판=빈 리스트
    for k in range(N): #세로만큼 가로를 중첩해서 판을 만든다
        a=input().split(' ') #주의: a에 들어가는 숫자의 수=M
        box[i].append(a) #정해진 층에 가로를 한줄씩 더해줍니다
'''
box[a][b][c]인 애의 값이 1이라면:
    만약 아래의 값이 -1or1이면:
        continue
    box[a-1][b][c]=1 (단 a=0일 경우 제외)
    box[a+1][b][c]=1 (단 a=M일 경우 제외)
    box[a][b-1][c]=1 (단 b=0일 경우 제외)
    box[a][b+1][c]=1 (단 b=N일 경우 제외)
    box[a][b][c-1]=1 (단 c=0일 경우 제외)
    box[a][b][c+1]=1 (단 c=H일 경우 제외)
    sum+=1 (이렇게 하루가 지나는것임)

근데 이거 약간 별모양으로 퍼져나가니까 규칙성이 충분히 있을만한데....ㅋㅋㅠ
'''

'''
특정 익은 토마토의 좌표가 하나 제시되고 모든 칸에 토마토가 차 있을 때의 수학적 규칙성 존재
'''
