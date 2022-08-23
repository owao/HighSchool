import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

mpl.rcParams['legend.fontsize']=10

fig=plt.figure()

ax=fig.gca(projection='3d')
theta=np.linspace(-4*np.pi,4*np.pi,100)
z=np.linspace(-2,2,100)

r=z**2+1
x=r*np.sin(theta)
y=r*np.cos(theta)
ax.plot(x,y,z,'ro', label='parametric curve') #ro를 지우면 파란 선그래프로 나옴
ax.legend()

plt.show()