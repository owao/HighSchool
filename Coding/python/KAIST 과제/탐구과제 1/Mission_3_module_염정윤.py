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
    if name not in book:
        print("Error: 등록되지 않은 연락처입니다.")
    if name in book:
        del book[name]
        print("연락처가 삭제되었습니다.")
        print()

def printbook(book):
    a=list(book.keys())
    for b in a:
        c=contact(b,book)
        c.print_c()

def modify(book):
    print("수정할 연락처를 입력하세요.")
    name1=str(input("name: "))
    if name1 not in book:
        print("Error: 등록되지 않은 연락처입니다.")
        print()
    if name1 in book:
        print("수정할 이름과 전화번호를 입력하세요.")
        name2=str(input("name: "))
        number=str(input("number: "))
        del book[name1]
        book[name2]=number    
        print("연락처가 수정되었습니다.")
        print()

def search(book):
    name=str(input("찾을 이름을 입력하세요."))
    tf=name in book
    if tf is True:
        print("전화번호는",book[name],"입니다.")
        print()
    if tf is False:
        print("Error: 등록되지 않은 연락처입니다.")
        print()

def readfile(book):
    n=str(input("열 파일의 이름을 입력하세요."))
    try:
        f=open(n)
        t=1
        for a in f:  
            if t%2==1:
                name=a
                t=t+1
                continue
            if t%2==0:
                number=a
                book[name]=number
                t=t+1
        print("파일을 연락처에 저장했습니다.")
        print()
    except:
        print("Error: 파일이 존재하지 않습니다.")

def writefile(book):
    t=open("전화번호부.txt","w")
    a=list(book.keys())
    for b in a:
        name="이름: %s"%(b)
        t.write(name)
        t.write("\n")
        number="전화번호: %s"%(book[b])
        t.write(number)
        t.write("\n")
        t.write("\n")
    print("기록된 전화번호부가 텍스트 파일로 생성되었습니다.")
    print()
    t.close
