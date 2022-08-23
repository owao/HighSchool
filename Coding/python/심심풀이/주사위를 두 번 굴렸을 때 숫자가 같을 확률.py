from random import *
a=[1,2,3,4,5,6]
same=0
diffrent=0
one=0
two=0
three=0
four=0
five=0
six=0

for i in range(1000000):
    n=choice(a)
    m=choice(a)
    if n==m:
        same=same+1
        if n==1:
            one+=1
        if n==2:
            two+=1
        if n==3:
            three+=1
        if n==4:
            four+=1
        if n==5:
            five+=1
        if n==6:
            six+=1
    else:
        diffrent+=1

print("억 번 6면 주사위를 굴렸을 때, 처음 숫자와 나중 숫자가 같을 확률: %.2f" %((same/1000000)*100))
print()
print("억 번 6면 주사위를 굴렸을 때, 같았던 숫자가 1일 확률: %.2f" %((one/1000000)*100))
print("억 번 6면 주사위를 굴렸을 때, 같았던 숫자가 2일 확률: %.2f" %((two/1000000)*100))
print("억 번 6면 주사위를 굴렸을 때, 같았던 숫자가 3일 확률: %.2f" %((three/1000000)*100))
print("억 번 6면 주사위를 굴렸을 때, 같았던 숫자가 4일 확률: %.2f" %((four/1000000)*100))
print("억 번 6면 주사위를 굴렸을 때, 같았던 숫자가 5일 확률: %.2f" %((five/1000000)*100))
print("억 번 6면 주사위를 굴렸을 때, 같았던 숫자가 6일 확률: %.2f" %((six/1000000)*100))
