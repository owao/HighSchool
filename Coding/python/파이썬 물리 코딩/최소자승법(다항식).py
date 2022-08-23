from numpy import *
from pylab import *

a=poly1d([1,2,3])
print(a)

b=poly1d([1,2,3,4])
print(b)

c=poly1d([1,-1,2],True)  #True: 저 세 값을 해로 가지는 다항식
print(c)
print(c[1]) #괄호 안 차수를 갖는 항의 계수 출력(1차항의 계수) - float로 나옴
print(int(c[0])) #0차항의 계수(=상수항) - int로 변환했음

X=array([1,2,3,4,5,6,7,8,9])
Y=array([2,3,3,5,6,7,7,10,11])
z=polyfit(X,Y,1) #추세선 그래프
print(z) #첫번째 값: 기울기, 두번째 값: y절편

p=poly1d(z)
print(p) #다항식으로 나온다! 왜냐면 z[0]이 기울기고(1차항의 계수) z[1]이 y절편이니까(상수항의 계수)

plot(X,Y,1) #1=직선
show() #점을 이은 그래프를 출력
