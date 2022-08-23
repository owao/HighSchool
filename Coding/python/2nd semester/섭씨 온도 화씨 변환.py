def CtoF(temp):
    return (temp*9)/5+32

temp=int(input("섭씨 온도를 입력하세요"))
out=CtoF(temp)
print("섭씨 %d는 화씨 %.2f입니다" %(temp, out))
