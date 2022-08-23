#import math
#print(math.sqrt(2))

#a=float(input("숫자"))
#b=math.sqrt(a)
#print(b)

#for x in range(1,10):
#    print(math.sqrt(x))

#for y in range(3,30):
#    b=y**2+40
#    print(math.sqrt(b))

'''
import turtle as t
t.speed(1)
t.dot(100,"skyblue")
t.fd(150)
t.dot(100,"skyblue")
t.lt(150)
t.fd(250)
t.home()
'''
'''
n = input("정수를 입력하세요:")
x = 0
for a in n:
    x+=int(a)
print(x)
'''
'''
while True:
    n=int(input())
    ps=round(n**0.5)+1
    print(ps)
'''
'''
def prime_number(n):
    if n == 2:
        return True
    if n < 2:
        return False
    if n % 2 == 0:
        return False
    ps = round(n**0.5) +1
    for ps in range(3, ps, 2):
        if n% ps == 0:
            return False
    else:
        return True


while True:
    sddd=int(input())
    if prime_number(sddd) is True:
        print("True")
    else:
        print("False")
'''

'''
a=int(input())
print(abs(a))
'''

'''
from random import *    #무작위로 뽑기 위해 random 모듈을 불러온다.

coin=["앞","뒤"]
front=0
back=0

for k in range(50): 
    n=choice(coin)
    if n=="앞":  
        front+=1   
    if n=="뒤":
        back+=1 
print("앞면: %d" %(front))
print("뒷면: %d" %(back))
'''

'''
#변수 2개 띄어쓰기로 구분해서 한번에받기
a,b=input().split(' ')
print(a)
print(b)
'''

'''
#리스트에 정수를 넣으면 정수가 나오는가... 정수가 나온다!
count=[]
p=0

for i in range(10):
	count.append(p)

print(count)
'''

'''
d=[1,2,3,4,5,6,7]
asdf=d[0]+5
d[0]=asdf
print(d)
'''

i=input().split(' ')
print(i)
print(int(i[0]))
