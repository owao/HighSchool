from 전화번호부 import *

print("1: 연락처 추가\n2: 연락처 삭제\n3: 연락처 수정\n4: 연락처 전체 출력\n5: 연락처 찾기\n6: 종료")
while True:
    n=int(input("명령을 입력하세요."))
    if n==1:
        add(book)
    if n==2:
        delete(book)
    if n==3:
        modify(book)
    if n==4:
        printbook(book)
    if n==5:
        name=str(input("찾을 이름을 입력하세요."))
        tf=name in book
        if tf is True:
            print("전화번호는",book[name],"입니다.")
            print()
        if tf is False:
            print("등록되지 않은 연락처입니다.")
            print()
    if n==6:
        print("종료합니다.")
        quit()
