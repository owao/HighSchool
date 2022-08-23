import math

s=float(input("원의 반지름을 입력하세요:"))
m=int(input("원의 넓이를 소수 몇 번째 자리까지 출력합니까?:"))

q=(math.pi)*(s**2)

print("원의 넓이는 %.f 입니다." %q)
