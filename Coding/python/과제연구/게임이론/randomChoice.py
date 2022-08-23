#랜덤 프로그램

import random

def suggest(l): #l은 방금 게임에서 준 금화의 수가 기록되는 리스트
    k=random.randrange(1,11)
    l.append(k)

def accept(a,l): #a는 리스트의 가장 마지막 값(상대가 가장 최근에 제시한), l은 이번 턴에서 반응을 저장하는 인스턴트 리스트
    i=["y","n"]
    k=random.choice(i)
    l.append(k)
