function [] = oddEven(n)
%숫자의 홀짝 판별
%oddEven(number)
if rem(n,2)==0
    disp('n은 짝수이다.')
else
    disp('n은 홀수이다.')
end

