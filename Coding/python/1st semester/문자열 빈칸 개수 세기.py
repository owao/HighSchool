n=input("문자열을 입력하시오: ")
count=0
for x in n:
    if x == ' ':
        count +=1
print(n, "빈 칸 갯수", count)
