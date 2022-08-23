from pylab import *
from class_formula import *

xy=array([0.01,0,0.01,0.01]) #시작점
a=RK2(foucalt_xy,0,15,xy,1000)
X1=a[0][:,0]
Y1=a[0][:,2]
t1=a[1]

plot(X1,Y1,'-')
legend(['Foucalt'])
xlabel('X')
ylabel('Y')
title('Foucalt')
show()