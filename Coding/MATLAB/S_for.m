function [sum] = S_for(n)
%1부터 n까지 세제곱 더하기
sum=0;
for i=1:n
    sum=sum+i^3;
end

