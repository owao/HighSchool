dan=2

while dan<=9:
    n=1
    while n<=9:
        value = dan * n
        print("%dx%d=%3d" %(dan, n, value))
        n=n+1
    print("========")
    dan+=1


#<ctrl>+<c> 누르면 무한루프 중지됨
