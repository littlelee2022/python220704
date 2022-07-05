# 부모 클래스 정의
class Person:
    # 초기화 메서드
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
    #인스턴스 메서드
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))

#자식 클래스 정의
class Student(Person):
    # 상속받은 메서드를 재정의( 덮어쓰기 overrride)
    def __init__(self, name, phoneNumber, subject, studentID):
        # self.name = name
        # self.phoneNumber = phoneNumber
        Person.__init__(self,name,phoneNumber)
        self.subject = subject
        self.studentID = studentID
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1}, subject: {2}, studentID: {3})".format(self.name, self.phoneNumber,self.subject, self.studentID))

# 내부값을 딕셔너리 형태로 보여주기
p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "빅데이터", "191122")
# print(p.__dict__)
# print(s.__dict__)

p.printInfo()
s.printInfo()

