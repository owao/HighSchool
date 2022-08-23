function [x,itnum] = gauss_seidel(A,b,x0,MaxIter)
%Gauss Seidel 방법으로 Ax=b의 해를 구하는 프로그램
%x0 : 초기값
%MaxIter : 최대반복횟수
%TOL : 오차한계
%b,x0는 열벡터
%itnum : 반복횟수

TOL=1e-5;

if nargin < 4 %반복횟수값이 안들어오면 지정해준다
    MaxIter=100;
end

if nargin<3 %초기값이 안들어오면 열벡터 크기로(행 개수) 맞춰준다
    x0=ones(size(b)); %jacobi랑 다르게 값이 1로 채워진 행렬
end

N=size(A,1); %A의 행 개수

x=x0; %값 복제(백업)

for i=1:Maxiter
    x(1)=(b(1)-A(1,2:N)*x(2:N))/A(1,1);
    for i=2:N-1
        temp=b(i)-A(i,1:i-1)*x(1:i-1)-A(i,i+1:N)*x(i+1:N);
        x(i)=temp/A(i,i);
    end
    x(N)=(b(N)-A(N,1:N-1)*x(1:N-1))/A(N,N);


end

