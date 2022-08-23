a=int(input("첫번째 숫자를 입력하세요:"))
b=int(input("두번째 숫자를 입력하세요:"))
hap=0
for i in range(a, b+1):
    hap +=i
print("입력한 두 수 사이의 합은 %d 입니다" %(hap))
