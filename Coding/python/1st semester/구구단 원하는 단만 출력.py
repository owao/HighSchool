print("구구단 출력 프로그램")
a=int(input("원하는 단을 입력하세요:"))

n=1
while n<=9:
    value=a*n
    print("%d*%d=%3d"%(a,n,value))
    n +=1
