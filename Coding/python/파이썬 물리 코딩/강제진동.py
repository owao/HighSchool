from numpy import *
from pylab import *
from class_formula import *

x_0=3
v_0=0
y_0=array([x_0,v_0])
a=RK2(forced_vib,0,30,y_0,1000) #강제진동
X=a[0][:,0]
t=a[1]

plot(t,X,'r-')
show()