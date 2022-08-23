function [x,iter]=fixedpoint_intiteration(g,x0,TOL.MaxIter)
%������ �ݺ����� ���� f(x)=0�� �ظ� ����
%���� f(x)=0�� g(x)=x�÷� �ٲپ�� ��.
%x0 : �ʱ� ������

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

