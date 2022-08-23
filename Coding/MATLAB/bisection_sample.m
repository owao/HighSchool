function [x,iter] = bisection_sample(f,a,b,TOL,MaxIter)
%이분법에 의해 f(x)=0의 해를 [a,b]에서 구함
%TOL : 오차한계
%MaxIter : 최대 반복횟수
%f : m파일로 주어질때는 반드시 문자열로. 예를 들어 식이
%testequation.m이라면 'testequation'으로 적어주어야 함.
%xm: 중간값
if nargin<5
    MaxIter=100;
end

if nargin<4
    TOL=1.e-5;
end

fa=feval(f,a);  %함숫값
fb=feval(f,b);

if (fa*fb>0)   %곱해서 양수가 되면 거른다
    error('It must be f(a)*f(b)<0');
end

for k=1:MaxIter  %반복횟수동안
    xm=(a+b)/2;  %중간값
    fm=feval(f,xm);  %중간값의 함숫값을 보고
    err=(b-a)/2;
    if(abs(fm)<TOL | abs(err)<TOL) break;
        elseif fm*fa>0, a=xm; fa=fm;  %비교해서 계속함
        else b=xm;
    end
end

x=xm;
iter=k;
