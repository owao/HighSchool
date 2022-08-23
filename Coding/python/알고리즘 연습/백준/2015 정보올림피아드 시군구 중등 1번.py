a=input().split() #char list
b=input().split() #char list

a=list(map(int, a)) #int 변환
b=list(map(int, b)) #int 변환

A_w=0 #A 승
B_w=0 #B 승

for i in range(0,10):
    p=a[i]
    q=b[i]
    if p>q:
        A_w += 1
    if p<q:
        B_w += 1
    else:
        continue

if A_w > B_w:
    print("A")
elif A_w < B_w: #else if 아님주의!!
    print("B")
else:
    print("D")
