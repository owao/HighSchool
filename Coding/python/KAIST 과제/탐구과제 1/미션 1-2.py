book={}

def add(book):
    print("추가할 연락처를 입력하세요.")
    name=str(input("name: "))
    number=str(input("number: "))
    book[name]=number
    print("연락처가 추가되었습니다.")
    print()
