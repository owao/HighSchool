from numpy import *
from pylab import *
from class_formula import *

x=0
y=0
vx=100
vy=100
y=array([x,vx,y,vx])

a=RK2(projectile,0,15,y,1000)
X1=a[0][:,0]
Y1=a[0][:,2]
t1=a[1]

a=RK2(projectile_air,0,15,y,1000)
X2=a[0][:,0]
Y2=a[0][:,2]
t2=a[1]

plot(X1,Y1,'-')
plot(X2,Y2,'r-')
legend(['Projectile','air resistance Projectile'])
xlabel('X')
ylabel('Y')
title('Projectile')
show()