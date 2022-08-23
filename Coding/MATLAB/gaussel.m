function [x] = gaussel(A,b)
% 가우스 소거법 : Ax=b
% A : nXn 행렬
% b : nX1 벡터

N=size(A,1); %행 크기
M=size(b,1); %행 크기

x=zeros(N,1); %위에서 구한 행으로 값이 0인 열벡터 생성
if(M~=N) %A행렬과 b행렬의 행 크기가 같지 않다면 에러(연산해야하니까)
    error('error');
end

W=zeros(N,N+1); %A보다 한 열 더 큰 행렬을 만듦(b를 붙이기위해)
W(1:N,1:N)=A(:,:); %A 붙여넣기
W(:,N+1)=b; %B 붙여넣기

for k=1:N-1
    %a_kk가 0인지 아닌지 조사하여 0인 경우 행을 바꾼다.
    for i=k:N %첫 루프때는 첫 열, 두번째 루프때는 둘째 열....
        if(W(i,k)~=0) %0이 아니라면 바로 연산하면 되니까 루프 탈출
            break;
        end
    end
    
    if(i~=k) %행바꾸기
        temprow=W(k,:); %k번째 열을 기준으로 k번째 
        W(k,:)=W(i,:); %유효한 값을 가진 i번째와 자리를 바꾼다
        W(i,:)=temprow; %k번째 열은 i 자리로 들어간다
    end
    
    %행을 바꾼 후에도 a_kk=0이면 해가 없는 경우이다.
    if(W(k,k)==0) %원하는대로 바꾼 후에도 자리가 0이다=해가 없다
        error('Singular system');
    else
        for i=k+1:N %11은 나머지행 1을 빼고 22는 나머지행 2를 빼고..
            m=W(i,k)/W(k,k); %비율대로 수를 맞춘다
        for j=k+1:N+1
            W(i,j)=W(i,j)-m*W(k,j); %맞춘 수를 빼서 0을 만든다
        end
        end
    end
end

if(W(N,N)==0) %x y z 에서 z 계수가 0인 경우 해 없음 처리
    error('Singular system');
else
    %후진대입법
    x(N)=W(N,N+1)/W(N,N);
    for k=N-1:-1:1 %삼각행렬이 나왔으면 해를 구한다
        x(k)=(W(k,N+1)-W(k,k+1:N)*x(k+1:N))/W(k,k);
    end
end

end

