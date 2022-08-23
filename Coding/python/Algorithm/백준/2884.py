a,b=map(int, input().split())

if b<45:  #분이 45분 이하면 시를 한 숫자 낮춤
    if a==0:
        a=23
    else:
        a=a-1
    b=b+15


elif b>=45:
    b=b-45


print(a,b)
