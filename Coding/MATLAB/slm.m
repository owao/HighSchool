function y = slm(c)
%SLM�� x=10^(-b)�� ���Ͽ� sn(x)/x�� ����Ѵ�
%���⿡�� b=1, ..., c�̴�.
format long
b=1:c;
x=10.^(-b);
y=(sin(x)./x)';