function [] = cramer_rule(a,b)
%크래머 공식
N=size(a,1); %행 길이(열 개수)
for i=1:N %열 순서대로(1번 열, 2번 열...)
    p=a; %행렬 복제(원본 백업)
    p(:,i)=b(:,:); %열 바꿔주기
    k=det(p)/det(a); %계산
    disp(k); %답 출력
end

end

