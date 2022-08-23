from numpy import *

def Euler_Method(f,a,b,y0,step):
	t=linspace(a,b,step)
	h=t[1]-t[0]
	Y=[y0]
	N=len(t)
	n=0
	y=y0
	while n<=N-2:
		y=y+h*f(y,t[n])
		Y.append(y)
		n=n+1
	Y=array(Y)
	return Y,t

def RK2(f,a,b,y0,step): #룽게 쿠타 방법
	t=linspace(a,b,step)
	h=t[1]-t[0]
	Y=[y0]
	N=len(t)
	n=0
	y=y0
	while n<=N-2:
		y_rk2=y+h*0.5*f(y,t[n])
		y=y+h*f(y_rk2,t[n]+h*0.5)
		Y.append(y)
		n=n+1
	Y=array(Y)
	return Y,t

def projectile(y,t): #포물선운동
	ay=(-9.8)
	ax=0
	vx=y[1]
	vy=y[3]
	f=array([vx,ax,vy,ay])
	return f

def projectile_air(y,t): #공기저항 있는 포물선운동
	m=10
	c=1
	ay=(-9.8)-(c/m)*y[3]
	ax=0-(c/m)*y[3]
	vx=y[1]
	vy=y[3]
	f=array([vx,ax,vy,ay])
	return f

def harmonic(y,t): #단진동(자유 비감쇠 운동):공기저항 고려 x(고려하면 자유 감쇠 운동)
	k=50 #용수철 상수
	m=200 #매달린 질량
	a=(-1*k/m)*y[0] #y[0]=초기위치
	v=y[1] #a로부터 구한 v
	f=array([v,a]) #다음 v가 나와야 함
	return f

def forced_vib(y,t): #강제진동
	k=200
	c=10
	m=50
	w=5 #외부에서 작용하는 힘의 각진동수
	F=500 #외부에서 작용하는 힘의 최대값
	a=(-1*k/m)*y[0]-(c/m)*y[1]+(F/m)*cos(w*t) #(F/m)*cos(w*t)은 외부 작용힘, 나머지 두 항은 감쇠진동
	v=y[1]
	f=array([v,a])
	return f

def foucalt_xy(xy,t): #푸코의 진자
	w=7 #진자의 각진동수
	W=0.6 #지구 자전 각속도
	c=(pi/5) #위도
	vx=xy[1] # 속도의 x성분
	ax=-(w**2)*xy[0]+2*W*xy[3]*sin(c)
	vy=xy[3] # 속도의 y성분
	ay=-(w**2)*xy[2]-2*W*xy[1]*sin(c)
	f=array([vx,ax,vy,ay])
	return f