function [] = bisection_mine(f,a,b)
%UNTITLED15 이 함수의 요약 설명 위치
%   자세한 설명 위치
fa=feval(f,a);
fb=feval(f,b);

if fa*fb>0
    disp('값을 다시 입력하세요.')
end

for i=1:50
    mid=a+b/2
    fm=feval(f,mid)

end

