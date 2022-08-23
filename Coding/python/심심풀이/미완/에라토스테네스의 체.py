print("에라토스테네스의 체를 이용해 소수를 구합니다.")
a=int(input("몇부터 시작할까요?"))
b=int(input("몇까지 구할까요?"))
c=2
k=[]
e=1

for d in range(a,b+1):
    k.append(d)


for q in k:
    for d in k:
        if d==c:
            continue
        if d%c==0:
            k.remove(d)
            continue
    k.sort()
    if e>=len(k):
        break
    c=k[e]
    e=e+1

if 1 in k:
    k.remove(1)

k.sort()

for d in k:
    print(d)

print("%d부터 %d 사이의 소수를 출력했습니다. 프로그램을 종료합니다." %(a,b))
