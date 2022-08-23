function [x2] = secant_mine(f,x0,x1)
%secant ¼ö·Å
MaxIter=100;
TOL=1.e-5;
x2=0;

for k=1:MaxIter
    f0=feval(f,x0);
    f1=feval(f,x1);
    
    x2=x1-(x1-x0)/(f1-f0)*f1;
    
    if(abs(x2-x1)<TOL)
        break;
    else
        x0=x1;
        x1=x2;
    end
end