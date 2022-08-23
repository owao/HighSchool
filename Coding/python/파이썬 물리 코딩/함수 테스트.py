def function(x):
	a=x**2
	return a

from numpy import *
from pylab import *

x=linspace(0,10)
y=function(x)
plot(x,y,'-')
show()