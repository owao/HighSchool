#특정 단어 X, 4자리~10자리 단어 중 하나만 나오면 됨(인간이 판정)
'''
def makeword():
    S_char=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    B_char=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    k=randint(4,10)
    U=[]
    word=""
    
    for i in range(k):
        if i==1:
            W=choice(B_char)
            U.append(W)
        if i>=1:
            W=choice(S_char)
            U.append(W)
            
    for i in U:   #리스트 속의 철자를 단어로 모음
        word+=i
        
    return word

from random import *
t=0 #횟수

while True:
    word=makeword()
    print(word)
    r=input("y/n")       #단어 판정(w.인간)
    if r=="n":           #틀리면 계속함ㅠ
        print()
        t+=1
        continue
    if r=="y":
        break
    else:
        continue

p=0
for i in word:
    p+=1
    
qwer=6*26**p

print("%d번 만에 정상적인 단어가 나왔습니다."%(t+1))
print("만일 이 단어를 원했을 시, 원래의 반복 기댓값은 %d회(6x(26^%d))였습니다."%(qwer,p))

'''

#특정 단어 O(개수 자유), 4자리 단어(컴이 판정)

def des_makeword():
    S_char=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    U=[]
    word=""
    
    for i in range(0,4):
        W=choice(S_char)
        U.append(W)
            
    for i in U:   #리스트 속의 철자를 단어로 모음
        word+=i
        
    return word


from random import *
t=0 #횟수
I=[]
while True:
    d=input("Choose word, please ")
    I.append(d)
    if d=="n":
        break

while True:
    word=des_makeword()
    print(word)
    if word not in I:
        print()
        t+=1
        continue
    if word in I:
        break

l=len(I)
qwer=26**4

print("%d번 만에 정상적인 단어가 나왔습니다."%(t+1))
print("만일 이 단어를 원했을 시, 원래의 반복 기댓값은 %.f회(26^4)/%d였습니다."%(qwer/l,l))
