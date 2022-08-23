function [x, iter] = secant_sample(f,x0,x1,TOL,MaxIter)
%secant 방법에 의해 f(x)=0의 해를 구함
%x0, x1 : 초기 추측값
%TOL : 오차한계
%MaxIter : 최대 반복횟수
%f : m파일로 주어질때는 반드시 문자열로. 예를 들어 식이
%testequation.m이라면 'testequation'으로 적어주어야 함.
if nargin<5
    MaxIter=100;
end

if nargin<4
    TOL=1.e-5;
end

x=x1;

for k=1:MaxIter
    f0=feval(f,x0);
    f1=feval(f,x1);
    
    x=x-(x1-x0)/(f1-f0)*f1;
    err=abs(x1-x0);
    if(err<TOL) break;
        else x0=x1; x1=x;
    end
end

iter=k;
