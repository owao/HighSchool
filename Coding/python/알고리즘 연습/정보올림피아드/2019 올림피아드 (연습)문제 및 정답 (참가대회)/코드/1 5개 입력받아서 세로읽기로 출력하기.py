l=[]
for k in range (5):
    a=list(input())
    l.append(a)
word=""

while True:
    if l==[[],[],[],[],[]]:
        break
    for k in range(5):
        if l[k]==[]:
            continue
        word=word+l[k][0]
        l[k].pop(0)

print(word)
