age=int(input("나이를 입력하세요 : "))

if age <= 7 or age >= 65 :
    fee=0
elif 8 <= age and age <= 13 :
    fee=450
else :
    fee=900
print("나이:%d --> 요금은 %d입니다" %(age, fee))
