function [] = bestscore()
%UNTITLED12 이 함수의 요약 설명 위치
%   자세한 설명 위치
a=[95.8 90.6 80.3 75.2 70.7 27.5 61.8];
name=['서경' '형석' '예원' '재환' '정윤' '영진' '종록']
score=0;
max=0;
maxnum=0;
for i=1:7
    score=a(1,i)
    if score>max
        max=score
        maxnum=i
disp(name(1,maxnum))
end