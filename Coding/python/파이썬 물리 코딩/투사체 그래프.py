from class_formula import *
from pylab import *

x=0
y=0
vx=100
vy=100
y=array([x,vx,y,vy])
b=RK2(projectile,0,15,y,100)
X=b[0][:,0]
Y=b[0][:,2]
t=b[1]

plot(X,Y,'-')
legend(['Projectile'])
xlabel('X')
ylabel('Y')
title('Projectile')
show()