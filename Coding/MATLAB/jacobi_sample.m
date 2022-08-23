function [x,itnum] = jacobi_sample(A,b,x0,MaxIter)
%Jacobi ������� Ax=b�� �ظ� ���ϴ� ���α׷�
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
    x0=zeros(size(b));
end

sizeofA=size(A,1); %A�� �� ����

x=x0; %�� ����(���)

%AT : a_ij/a_ii, �밢���Ҵ� 0
%bt : b_j/aii

for i=1:sizeofA %���ȣ
    for j=1:sizeofA %����ȣ
        if j~=i %���ȣ�� ����ȣ�� �ٸ��ٸ�
            AT(i,j)=-A(i,j)/A(i,i);
        end
    end
    bt(i,:)=b(i,:)/A(i,i);
end

for iter=1:MaxIter %���Ƚ��
    x=AT*x+bt; %����� �������� ������
    if nargout==0 %���� ��ȯ(�����ݷ� ������ ��ȯx)
        x;
    end
    if norm(x-x0)<TOL %�������� �̳��� ������
        itnum=iter; %�ݺ�Ƚ�� ���
        break;
    end
    x0=x;
end

end

