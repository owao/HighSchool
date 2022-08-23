function [] = grade(g)
%등급 출력 함수
if (100>=g)&(g>=90)
    disp('A')
elseif (90>g)&(g>=80)
    disp('B')
elseif (80>g)&(g>=70)
    disp('C')
elseif (70>g)&(g>=60)
    disp('D')
elseif (60>g)&(g>=0)
    disp('F')
else
    disp('정확한 점수를 넣어주세요')
end

