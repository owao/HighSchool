function [x, iter] = secant_sample(f,x0,x1,TOL,MaxIter)
%secant ����� ���� f(x)=0�� �ظ� ����
%x0, x1 : �ʱ� ������
%TOL : �����Ѱ�
%MaxIter : �ִ� �ݺ�Ƚ��
%f : m���Ϸ� �־������� �ݵ�� ���ڿ���. ���� ��� ����
%testequation.m�̶�� 'testequation'���� �����־�� ��.
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
