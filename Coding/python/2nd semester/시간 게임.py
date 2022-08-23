import random
import time


while True:
    print("** 시간 측정 프로그램 **")
    print("준비되면 <Enter>를 누르세요")

    input()
    test = random.randint(5,11)
    start = time.time()

    print("%d초 후 <Enter>를 누르세요" %test)
    input()
    end = time.time()

    print("목표시간: %.2f 초" %test)
    print("실제시간: %.2f 초" %abs(end-start))

    print()
