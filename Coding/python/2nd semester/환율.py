def ch(a,b):
    if b==0:
        b=1200
    return a*b


A=int(input("용돈을 입력하세요($):"))
B=float(input("오늘의 환율은? (모르면 0 입력):"))
s=ch(A,B)
print("%d달러는 %d원입니다" %(A,s))
