#장소명=(거리)[아트센터, 급식실, 교과교실, 도서관, 햇살마당, 운동장, 체육관]
#노드가 없거나 자기 자신일 경우 0

from math import *

def counting(a,sum,n):
    artcenter=[0,sqrt((57+8*sqrt(34))/2),0,0,0,0,0]
    cafeteria=[sqrt((57+8*sqrt(34))/2),0,2,0,sqrt(29/4),0,0]
    classroom=[0,2,0,2,sqrt(29/4),sqrt(61/40),sqrt(24)]
    library=[0,0,2,0,0,0,0]
    sunlightYard=[0,sqrt(29/4),sqrt(29/4),0,0,4,sqrt(61/40)]
    playground=[0,0,sqrt(61/40),0,4,0,sqrt(5/4)]
    gym=[0,0,sqrt(24),0,sqrt(61/40),sqrt(5/4),0]

    setting=[artcenter,cafeteria,classroom,library,sunlightYard,playground,gym]

    b=0 #길이
    s=0

    for i in setting[n]:
        if a[s]==0:
            s=s+1
            continue
        if b>0:
            if i<b and i>0:
                b=i
                n=s
            else:
                continue
        else:
            if i>0:
                b=i
                n=s
        s=s+1

    a[n]=0 #지나간 장소는 0으로 표시
    sum=sum+b

    if n==4:
        sum=sum+b



artcenter=[0,sqrt((57+8*sqrt(34))/2),0,0,0,0,0]
cafeteria=[sqrt((57+8*sqrt(34))/2),0,2,0,sqrt(29/4),0,0]
classroom=[0,2,0,2,sqrt(29/4),sqrt(61/40),sqrt(24)]
library=[0,0,2,0,0,0,0]
sunlightYard=[0,sqrt(29/4),sqrt(29/4),0,0,4,sqrt(61/40)]
playground=[0,0,sqrt(61/40),0,4,0,sqrt(5/4)]
gym=[0,0,sqrt(24),0,sqrt(61/40),sqrt(5/4),0]

setting=[artcenter,cafeteria,classroom,library,sunlightYard,playground,gym]

a=[1,1,1,1,1,1,1] #지나가지 않은 장소를 1로, 지나간 장소를 0으로 표시
sum=0 #길이 총합
n=0 #위치

while True:
    n=counting(a,sum,n)
    if a==[0,0,0,0,0,0,0]:
        break
    
print(sum)
