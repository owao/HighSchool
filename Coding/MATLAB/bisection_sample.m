function [x,iter] = bisection_sample(f,a,b,TOL,MaxIter)
%�̺й��� ���� f(x)=0�� �ظ� [a,b]���� ����
%TOL : �����Ѱ�
%MaxIter : �ִ� �ݺ�Ƚ��
%f : m���Ϸ� �־������� �ݵ�� ���ڿ���. ���� ��� ����
%testequation.m�̶�� 'testequation'���� �����־�� ��.
%xm: �߰���
if nargin<5
    MaxIter=100;
end

if nargin<4
    TOL=1.e-5;
end

fa=feval(f,a);  %�Լ���
fb=feval(f,b);

if (fa*fb>0)   %���ؼ� ����� �Ǹ� �Ÿ���
    error('It must be f(a)*f(b)<0');
end

for k=1:MaxIter  %�ݺ�Ƚ������
    xm=(a+b)/2;  %�߰���
    fm=feval(f,xm);  %�߰����� �Լ����� ����
    err=(b-a)/2;
    if(abs(fm)<TOL | abs(err)<TOL) break;
        elseif fm*fa>0, a=xm; fa=fm;  %���ؼ� �����
        else b=xm;
    end
end

x=xm;
iter=k;
