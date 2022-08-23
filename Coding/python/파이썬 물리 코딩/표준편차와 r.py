def Sigma_y(x,y): #표준편차 구하기 - x와 y값을 넣음
	y0=polyfit(x,y,1) #추세선이 되는 2차함수를 찾아줌
	p=poly1d(y0) #직선의 방정식
	y_=p(x) #y의 이론값(모델값)
	d=y-y_ #실험값과 이론값의 차이
	N=len(x) #원소갯수의 파악
	sigma=sqrt((sum(square(d)))/(N-2))
	return sigma

def R_square(x,y): #r제곱값
	y_m=mean(y)*ones(len(x)) #y데이터의 평균값
	a=sum(square(y-y_m)) #y데이터와 평균값의 차
	y0=polyfit(x,y,1) #데이터를 기반으로 최소자승법
	p=poly1d(y0)
	b=sum(square(y-p(x))) #카이제곱값
	return ((a-b)/a)

from pylab import *

X=array([1,2,3,4,5,6,7,8,9])
Y=array([2,3,3,5,6,7,7,10,11])
z=polyfit(X,Y,1)
p=poly1d(z)
print(z) #추세선을 다항식으로 출력

y=p(X)
errorbar(X,Y, yerr=Sigma_y(X,Y), fmt='o')
plot(X,y,'-')
ylim([0,12])
show()