menu = {"짜장면":4000, "짬뽕":4000, "탕수육":15000, "깐풍기":20000}
a=input("음식명")
if a in menu:
    print("가격은 %d입니다" %menu[a])
else:
    print("%s는 판매하지 않습니다" %a)
