def fib(n):
    if n>1:
        return fib(n-1)+fib(n-2)
    else:
        return n
'''
for i in range(2, 5):
    print(fib(i))


a=int(input())
print(fib(a))


'''


b=int(input("범위의 시작점을 입력하세요"))
c=int(input("범위의 마지막 숫자를 입력하세요"))
print("%d부터 %d번째 피보나치 수열을 출력합니다." %(b,c))

for i in range(b, c+1):
    print(fib(i))
