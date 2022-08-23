while True:
    a=int(input("첫번째 숫자:"))
    if a==0:
        break
    b=int(input("두번째 숫자:"))
    hap=a+b
    print("%d+%d=%d" %(a,b,hap))
print("프로그램 종료")


# break : 특정 조건 만족 시 프로그램 종료





hap=0
for i in range(1, 101):
    if i%3==0:
        continue

    hap +=i

print("1~100까지의 합(3의배수 제외) : %d" %(hap))

# continue : 특정 조건 만족 시 이후 조건 없이 처음으로 다시 되돌아감






for x in range(0,51,5):
    print(x, end='/')

print()


for x in range(10, 0, -1):
    print(x, end="초")


# print(n,end='x') : for문을 진행하면서 n값들 사이에 x를 표기하여라






