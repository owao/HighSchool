from random import *

L=[]
result=[]
while True:
    a=input("단어를 입력하세요. ")
    if a==" ":
        break
    L.append(a)

while True:
    if len(result)==10:
        break
    b=randrange(0,len(L)-1)
    if L[b] in result:
        continue
    result.append(L[b])

for i in result:
    print(i)
