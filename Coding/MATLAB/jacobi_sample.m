function [x,itnum] = jacobi_sample(A,b,x0,MaxIter)
%Jacobi 방법으로 Ax=b의 해를 구하는 프로그램
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
    x0=zeros(size(b));
end

sizeofA=size(A,1); %A의 행 개수

x=x0; %값 복제(백업)

%AT : a_ij/a_ii, 대각원소는 0
%bt : b_j/aii

for i=1:sizeofA %행번호
    for j=1:sizeofA %열번호
        if j~=i %행번호와 열번호가 다르다면
            AT(i,j)=-A(i,j)/A(i,i);
        end
    end
    bt(i,:)=b(i,:)/A(i,i);
end

for iter=1:MaxIter %계산횟수
    x=AT*x+bt; %행렬을 구했으니 덮어씌운다
    if nargout==0 %과정 반환(세미콜론 있으면 반환x)
        x;
    end
    if norm(x-x0)<TOL %오차범위 이내로 들어오면
        itnum=iter; %반복횟수 백업
        break;
    end
    x0=x;
end

end

