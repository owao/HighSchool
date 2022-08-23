with open('명사.txt') as f:
    noun=f.read().split('\n')
with open('동사.txt') as f:
    verb=f.read().split('\n')
with open('조사.txt') as f:
    asdf=f.read().split('\n')

from random import *


def suffix(a,b,c,q,p):    #a는 판별, b는 출력한 단어, c는 출력한 조사, q은 조사 리스트, p는 참조 리스트
    qwer=q.index(c)
    if a=="y":
        p[qwer][0].append(b[-1])    #조사 리스트의 c라는 조사는 b 단어의 맨 끝 글자일 때 나와야 한다는 걸 가르친다
    if a=="n":
        #c와 b[-1]이 맞지 않으므로 건너뛴다는걸 습득시킨다
        o=0


l=[]
i=len(asdf)
for k in range(i):
    l.append(0)

while True:
    a=choice(noun)
    b=choice(asdf)
    c=choice(noun)
    d=choice(asdf)
    e=choice(verb)
    print("%s%s %s%s %s" %(a,b,c,d,e))
    
    p=input() #첫번째조사
    q=input() #두번째조사
    suffix(p,a,b,asdf,l)
    suffix(q,c,d,asdf,l)

noun.close()
verb.close()
d.close()
