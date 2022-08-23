import turtle as t

n=int(input("원하는 도형이 몇각형인지 숫자를 입력하세요:"))
len=int(input("한변의 길이를 입력하세요:"))

count=1

while count<=n:
        t.forward(len)
        t.left(360/n)

        count+=1
