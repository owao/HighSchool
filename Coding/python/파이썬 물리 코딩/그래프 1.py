from pylab import * #pylab : 그래프 그리기

A=array([1,2,3,4,5,6])
B=array([2,4,3,5,2,3])
C=array([2,3,1,4,2,5])

plot(A,B,'o',A,C,'-') #(A,B)는 점을 찍고 (A,C)는 선그래프로 그려라


legend(['dot','line']) #그래프 이름을 라벨링, 위의 그래프 명령과 순서를 맞춰야 함 (loc=''로 위치 지정 가능-upper/lower right/left)
xlabel('x_label')
ylabel('y_label')
title('Title')


show()