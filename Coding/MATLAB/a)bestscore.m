function [] = bestscore()
%UNTITLED12 �� �Լ��� ��� ���� ��ġ
%   �ڼ��� ���� ��ġ
a=[95.8 90.6 80.3 75.2 70.7 27.5 61.8];
name=['����' '����' '����' '��ȯ' '����' '����' '����']
score=0;
max=0;
maxnum=0;
for i=1:7
    score=a(1,i)
    if score>max
        max=score
        maxnum=i
disp(name(1,maxnum))
end