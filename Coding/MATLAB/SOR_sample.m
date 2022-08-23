function [x,itnum] = SOR_sample(A,b,x0)
%successive over-relaxation(newton�� ����ȣȯ)
%x0 : �ʱⰪ
%MaxIter : �ִ�ݺ�Ƚ��
%TOL : �����Ѱ�
%b,x0�� ������
%itnum : �ݺ�Ƚ��

TOL=1e-5;
x0=ones(size(b));
MaxIter=100;
omega=1.3;

N=size(A,1);
x=x0;

for iter=1:MaxIter
    x(1)=x(1)-omega*(A(1,1:N)*x(1:N)-b(1))/A(1,1);
    for i=2:N-1
        temp=A(i,i-1)*x(1:i-1)+A(i,i:N)*x(i:N)-b(i);
        x(i)=x(i)-omega*temp/A(i,i);
    end
    x(N)=x(N)-omega*(A(N,1:N)*x(1:N)-b(N))/A(N,N);
    itnum=iter;
    norm(x-x0);
    if norm(x-x0)<TOL
        break;
    end;
x0=x;
end

