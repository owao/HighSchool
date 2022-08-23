import random

with open('valid.txt') as f:
    diction = f.read().split('\n')

def say(log):
    
    words=[]
    t=[]
    
    if log==[]:
        k=random.choice(diction)
        diction.remove(k)
        return k
    
    for w in diction:
        if w[0]==log[-1][-1]:
            if w in log:
                continue
            words.append(w)
            
    #words 정렬_긴 단어순
    x=0
    for u in words:
        y=len(u)
        if x>=y:
            continue
        else:
            x=y
    for i in words:
        if len(i)==y:
            words.remove(i)
            words.insert(0,i)
            break
        else:
            continue
    
    for s in words:
        if s[-1]==log[-1][0]:
            t.append(s)
        
    #t 정렬_긴 단어순
    x=0
    for u in t:
        y=len(u)
        if x>=y:
            continue
        else:
            x=y
    for i in t:
        if len(i)==y:
            t.remove(i)
            t.insert(0,i)
            break
        else:
            continue
    
    if t != []:
        answer=t[0]
    else:
        if words==[]:
            print("상대 단어의 끝말로 시작하는 단어가 더 이상 없습니다(상대 단어가 한방단어입니다)")
            exit
        else:
            answer=words[0]
        
    diction.remove(answer)
    return answer

def name():
    return "9기 염정윤"
