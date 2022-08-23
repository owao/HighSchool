from Mission_3_module_염정윤 import *

print("1: 연락처 추가\n2: 파일에 있는 연락처 추가\n3: 연락처 삭제\n4: 연락처 수정\n5: 연락처 전체 출력\n6: 파일로 연락처 저장\n7: 연락처 찾기\n8: 종료")
while True:
    n=int(input("명령을 입력하세요."))
    if n==1:
        add(book)
    if n==2:
        readfile(book)
    if n==3:
        delete(book)
    if n==4:
        modify(book)
    if n==5:
        printbook(book)
    if n==6:
        writefile(book)
    if n==7:
        search(book)
    if n==8:
        print("종료합니다.")
        quit()
