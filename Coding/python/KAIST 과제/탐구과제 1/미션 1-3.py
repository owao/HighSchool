def delete(book):
    print("삭제할 이름을 입력하세요.")
    name=str(input("name: "))
    del book[name]
    print("연락처가 삭제되었습니다.")
    print()
