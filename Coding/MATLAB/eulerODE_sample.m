function [] = eulerODE_sample()
%미분방정식 euler 방법
%y(x)=-(x+1)+2e^x 식에 관한 solution (2e^x=2exp(x))
%differential equation : y'=x+y, y(0)=1

%mesh size
N=10;
x=linspace(0,1,N+1);
y=zeros(1,N+1);
h=1./N;
y(1)=1;
exact=0;
error=0;

disp(sprintf('x(i+1) \t\t exact \t\t y(i+1) \t\t error'))

for i=1:N
    y(i+1)=y(i)+h*(x(i)+y(i));
    exact=-x(i+1)-1.+2.*exp(x(i+1));
    error=y(i+1)-exact;
    disp(sprintf('%f\t %f\t %f\t %f \n',x(i+1),exact,y(i+1),error))
    plot(x,y,'-*r')
end
end

