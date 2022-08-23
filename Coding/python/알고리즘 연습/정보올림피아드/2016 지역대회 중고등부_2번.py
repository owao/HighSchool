b=1
for a in range(1,20):
    b=b*a

c=hex(b)

p=[]

for q in str(c):
    p.append(q)

p.reverse()
poiu=0

for qwer in p:
    if qwer=="0":
        poiu=poiu+1
        continue
    if qwer!="0":
        print(poiu)
        break
