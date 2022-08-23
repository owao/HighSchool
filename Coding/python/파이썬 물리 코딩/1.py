from numpy import *
from pylab import *
x=linspace(1,10,50) #linspace(1부터 10까지 50개 분할로 값을 정함)
y=x*x
title("my first praph")
xlabel("Time(fortnights)")
ylabel("Distance(furlongs)")
xlim(0,10) #x축 길이
ylim(0,100) #y축 길이
plot(x,y,'r-') #plot(점찍기), ro(빨간 점), bo(파란 점), g-(초록 선)
show()

#ctrl+B 누르면 실행됨