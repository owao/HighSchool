function [] = bisection_mine(f,a,b)
%UNTITLED15 �� �Լ��� ��� ���� ��ġ
%   �ڼ��� ���� ��ġ
fa=feval(f,a);
fb=feval(f,b);

if fa*fb>0
    disp('���� �ٽ� �Է��ϼ���.')
end

for i=1:50
    mid=a+b/2
    fm=feval(f,mid)

end

