#1번째-모든 공에 대해 모든 공을 계산하기
#기각 사유: Timeout
'''
N=int(input()) #값의 개수
c_l=[] #색깔
s_l=[] #크기
for i in range(N):
    a,b=input().split(' ')
    c_l.append(int(a))
    s_l.append(int(b))

poiu=0
for ballnumber in range(N): #어떤 공을 고름(순서대로)
    for nextball in range(N): #어떤 공에 대해 공이 잡을 수 있는 크기를 계산
        a=int(c_l[nextball])
        b=int(c_l[ballnumber])
        c=int(s_l[ballnumber])
        d=int(s_l[nextball])
        if a==b:
            continue
        else:
            if c<=d:
                continue
            if c>=d:
                poiu=poiu+d
    print(poiu)
    poiu=0
'''

#2번째-한번 계산한 후 양쪽에 값 배분
#기각 사유: Timeout
'''
N=int(input()) #값의 개수
c_l=[] #색깔
s_l=[] #크기
count=[]
p=0

for i in range(N):
    a,b=input().split(' ')
    c_l.append(int(a))
    s_l.append(int(b))
    count.append(p)

for base in range(N): #어떤 공을 고름(순서대로)
    for cont in range(base, N): #어떤 공에 대해 공이 잡을 수 있는 크기를 계산(자신부터 자기 뒷번호까지)
        a=int(c_l[base]) #기준 공(색)
        b=int(c_l[cont]) #비교군 공(색)
        c=int(s_l[base]) #기준 공(크기)
        d=int(s_l[cont]) #비교군 공(크기)
        if a==b: #두 공의 색이 같다
            continue #크기를 더하지 않고 건너뛴다
        else: #색이 다르다면
            if c==d: #두 공의 크기가 같다면
                continue #일단 패스!
            if c<d: #기준이 되는 공이 작다면
                asdf=count[cont]+s_l[base] #count[cont]에 s_l[base]의 값을 더해준다
                count[cont]=asdf
            if c>d: #기준이 되는 공이 크다면
                asdf=count[base]+s_l[cont] #count[base]에 s_l[cont]의 값을 더해준다
                count[base]=asdf

for i in range(N):
    print(count[i])
'''
