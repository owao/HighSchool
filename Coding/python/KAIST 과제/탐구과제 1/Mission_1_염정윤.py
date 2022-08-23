class contact:
    def __init__(self,name,book):
        self.name=name
        self.number=book[name]
    def callnumber(self,name,book):
        self.name=name
        self.number=book[name]
    def print_c(self):
        print("이름: {0}\n전화번호: {1}\n----------".format(self.name, self.number))

book={}

def add(book):
    print("추가할 연락처를 입력하세요.")
    name=str(input("name: "))
    number=str(input("number: "))
    book[name]=number
    print("연락처가 추가되었습니다.")
    print()

def delete(book):
    print("삭제할 이름을 입력하세요.")
    name=str(input("name: "))
    del book[name]
    print("연락처가 삭제되었습니다.")
    print()

def printbook(book):
    a=list(book.keys())
    for b in a:
        c=contact(b,book)
        c.print_c()
    
add(book)
add(book)
add(book)
delete(book)
printbook(book)
