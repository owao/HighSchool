import random

def compare(a,b):
    k=0
    for s in b:
        if s in a:
            k=k+1
    return k

def comparetwo(a,b,c,d,e,f,g,h,i,j):
    u=[a,b,c,d,e,f,g,h,i,j]
    u.sort(reverse=True)
    return u.index(a)+1

num=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

while True:
    player=[]
    for x in range(5):
        a=int(input("숫자를 입력하세요: "))
        player.append(a)

    rone=random.sample(range(1,15),5)
    rtwo=random.sample(range(1,15),5)
    rthree=random.sample(range(1,15),5)
    rfour=random.sample(range(1,15),5)
    rfive=random.sample(range(1,15),5)
    rsix=random.sample(range(1,15),5)
    rseven=random.sample(range(1,15),5)
    reight=random.sample(range(1,15),5)
    rnine=random.sample(range(1,15),5)
    prize=random.sample(range(1,15),5)

    player_result=compare(player,prize)
    rone_result=compare(rone,prize)
    rtwo_result=compare(rtwo,prize)
    rthree_result=compare(rthree,prize)
    rfour_result=compare(rfour,prize)
    rfive_result=compare(rfive,prize)
    rsix_result=compare(rsix,prize)
    rseven_result=compare(rseven,prize)
    reight_result=compare(reight,prize)
    rnine_result=compare(rnine,prize)

    print("이번 당첨 번호: %s" %(prize))
    print("당신의 숫자: %s 맞힌 개수: %d" %(player,player_result))
    print("로봇 1의 숫자: %s 맞힌 개수: %d" %(rone,rone_result))
    print("로봇 2의 숫자: %s 맞힌 개수: %d" %(rtwo,rtwo_result))
    print("로봇 3의 숫자: %s 맞힌 개수: %d" %(rthree,rthree_result))
    print("로봇 4의 숫자: %s 맞힌 개수: %d" %(rfour,rfour_result))
    print("로봇 5의 숫자: %s 맞힌 개수: %d" %(rfive,rfive_result))
    print("로봇 6의 숫자: %s 맞힌 개수: %d" %(rsix,rsix_result))
    print("로봇 7의 숫자: %s 맞힌 개수: %d" %(rseven,rseven_result))
    print("로봇 8의 숫자: %s 맞힌 개수: %d" %(reight,reight_result))
    print("로봇 9의 숫자: %s 맞힌 개수: %d" %(rnine,rnine_result))

    u=comparetwo(player_result,rone_result,rtwo_result,rthree_result,rfour_result,rfive_result,rsix_result,rseven_result,reight_result,rnine_result)
    print("당신은 %d 등!" %(u))

    s=input("계속하시겠습니까? (y/n) ")
    if s=="y":
        continue
    if s=="n":
        break
