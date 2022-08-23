function y = slm(c)
%SLM은 x=10^(-b)에 대하여 sn(x)/x를 계산한다
%여기에서 b=1, ..., c이다.
format long
b=1:c;
x=10.^(-b);
y=(sin(x)./x)';