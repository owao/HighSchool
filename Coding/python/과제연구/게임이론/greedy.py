#원하는 비율만큼 받지 못하면 거부

import random

def suggest(a,l):  #a는 게임이 진행된 횟수(1~10), l은 방금 게임에서 준 금화의 수가 기록되는 리스트
    k=random.randrange(0,5)
    l.append(k) #본인이 원하는 비율만큼 우선 가져가고 남은 것 중에서 줌. 여기서 원하는 비율은 60% 이상으로 고정

def accept(a,l): #a는 리스트의 가장 마지막 값(상대가 가장 최근에 제시한), l은 그동안 턴들의 반응을 저장하는 리스트
    if a>=6:
        l,append('y')
    else:
        l.append('n')
