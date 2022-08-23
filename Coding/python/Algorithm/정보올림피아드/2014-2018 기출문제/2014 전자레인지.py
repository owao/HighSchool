time=int(input())
An=int(time/300) #A 횟수
Bn=int((time%300)/60) #B 횟수
Cn=int(((time%300)%60)/10)#C 횟수
if int(((time%300)%60)%10)!= 0:
    print(-1)
else:
    print(An, Bn, Cn)
