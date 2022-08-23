function [x,iter]=fixedpoint_intiteration(g,x0,TOL.MaxIter)
%고정점 반복법에 의해 f(x)=0의 해를 구함
%먼저 f(x)=0을 g(x)=x꼴로 바꾸어야 함.
%x0 : 초기 추측값

if nargin<4
    MaxIter=100;
end

if nargin<3
    TOL=1.e-5;
end

for k=1:MaxIter
    x=x0;
    x=feval(g,x);
    err=abs(x-x0);
    if(err<TOL) break;
    else x0=x;
    end
end

iter=k;
end

