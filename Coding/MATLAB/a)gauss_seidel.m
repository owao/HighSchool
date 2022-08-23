function [x,itnum] = gauss_seidel(A,b,x0,MaxIter)
%Gauss Seidel ������� Ax=b�� �ظ� ���ϴ� ���α׷�
%x0 : �ʱⰪ
%MaxIter : �ִ�ݺ�Ƚ��
%TOL : �����Ѱ�
%b,x0�� ������
%itnum : �ݺ�Ƚ��

TOL=1e-5;

if nargin < 4 %�ݺ�Ƚ������ �ȵ����� �������ش�
    MaxIter=100;
end

if nargin<3 %�ʱⰪ�� �ȵ����� ������ ũ���(�� ����) �����ش�
    x0=ones(size(b)); %jacobi�� �ٸ��� ���� 1�� ä���� ���
end

N=size(A,1); %A�� �� ����

x=x0; %�� ����(���)

for i=1:Maxiter
    x(1)=(b(1)-A(1,2:N)*x(2:N))/A(1,1);
    for i=2:N-1
        temp=b(i)-A(i,1:i-1)*x(1:i-1)-A(i,i+1:N)*x(i+1:N);
        x(i)=temp/A(i,i);
    end
    x(N)=(b(N)-A(N,1:N-1)*x(1:N-1))/A(N,N);


end

