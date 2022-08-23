#팃포탯

def suggest(a,b,l):  #a는 게임이 진행된 횟수(1~10), b는 방금 상대의 반응, l은 방금 게임에서 준 금화의 수가 기록되는 리스트
    if a==1:
        l.append(5) #첫 턴에는 무조건 5개 배분
    else if b=='n': #상대가 내 제안을 거부했다면 나도 안 준다
        l.append(0)
    else:
        l.append(5)

def accept(a,l): #a는 리스트의 가장 마지막 값(상대가 가장 최근에 제시한), l은 이번 턴에서 반응을 저장하는 인스턴트 리스트
    if a<5:
        l.append('n')
    if a>=5:
        l.append('y')
