class contact:
    def __init__(self,name,book):
        self.name=name
        self.number=book[name]
    def callnumber(self,name,book):
        self.name=name
        self.number=book[name]
    def print_c(self):
        print("이름: {0}\n전화번호: {1}\n----------".format(self.name, self.number))
