function [] = cramer_rule(a,b)
%ũ���� ����
N=size(a,1); %�� ����(�� ����)
for i=1:N %�� �������(1�� ��, 2�� ��...)
    p=a; %��� ����(���� ���)
    p(:,i)=b(:,:); %�� �ٲ��ֱ�
    k=det(p)/det(a); %���
    disp(k); %�� ���
end

end

