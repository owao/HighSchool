from pylab import *

A=array([1,2,3,4,5,6])
B=array([2,4,3,5,2,3])
C=array([2,3,1,4,2,5])

subplot(2,1,1) #그래프를 분할해서 표현. (행의 개수,열의 개수,몇 번째 칸에 그릴지)

legend(['dot'])
xlabel('x_label A')
ylabel('y_label B')
title('Title')
plot(A,B,'o')

subplot(2,1,2) #그래프를 분할해서 표현. (행의 개수,열의 개수,몇 번째 칸에 그릴지)

legend(['line'])
xlabel('x_label A')
ylabel('y_label C')
title('Title')
plot(A,B,'r-')

show() #그래프를 여러개 한꺼번에 보여주려면 출력은 한번만subplot(2,1,1) #그래프를 분할해서 표현. (행의 개수,열의 개수,몇 번째 칸에 그릴지)

legend(['dot'])
xlabel('x_label A')
ylabel('y_label B')
title('Title')
plot(A,B,'o')
show()