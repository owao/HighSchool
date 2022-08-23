print("입력받은 숫자들로 리스트를 작성합니다. 0을 누르면 종료됩니다. 1~1000 사이의 수가 아닌 것은 입력해도 리스트에 들어가지 않습니다.")
num_list = list()
while True:
    number=int(input("Enter Number: "))
    if number == 0:
        break
    if number > 1000 or number < 1:
        continue
    num_list.append(number)

print("입력값:",num_list)
num_list.sort()
print("최솟값:", num_list[0], "최댓값:", num_list[-1])
