from random import *

a=0
x=[]
y=[]

while a<=10:
    x.append(a)
    y.append(a)
    a=a+0.01

x.sort()
y.sort()

c=[]

for s in x:
    q=choice(y)
    y.remove(q)
    f=[s,q]
    c.append(f)

t=open("단조형태가 아닌 역함수에 대해.xlsx","w")
for u in c:
    n=str(u)
    t.write(n)
    t.write("\n")
t.close
