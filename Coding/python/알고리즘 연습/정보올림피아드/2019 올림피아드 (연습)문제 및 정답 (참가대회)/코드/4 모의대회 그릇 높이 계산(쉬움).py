a=input()
b=len(a)
sum=10
for i in range(1,b):
    c=a[i]
    d=a[i-1]
    if c!=d:
        sum+=10
    if c==d:
        sum+=5
print(sum)
