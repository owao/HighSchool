#본인이 한 번이라도 0개를 받으면 상대를 무조건 거부

import random

def suggest(a,l):  #a는 게임이 진행된 횟수(1~10), l은 방금 게임에서 준 금화의 수가 기록되는 리스트
    k=random.randrange(3,11) #3~10개 중 주고싶은대로 줌
    l.append(k)

def accept(a,l): #a는 리스트의 가장 마지막 값(상대가 가장 최근에 제시한), l은 그동안 턴들의 반응을 저장하는 리스트
    if 'n' in l:
        l.append('n') #이전에 0개를 받은 적 있다면 거절
    else if a==0:
        l.append('n') #0개를 받는다면 거절
    else:
        l.append('y') #이외에는 수락
