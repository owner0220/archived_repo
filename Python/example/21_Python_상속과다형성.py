class Person:
    def __init__(self,name,phoneNumber):
        self.name=name
        self.phoneNumber=phoneNumber
    def printInfo(self):
        print("Info Name : {},phoneNumber : {}".format(self.name,self.phoneNumber))

class Student(Person):
    def __init__(self,name,phoneNumber,subject,StudentId):
        Person.__init__(self,name,phoneNumber)
        self.subject=subject
        self.StudentId=StudentId
    
    def printInfo(self):
        print("info Name:{},phoneNumber:{}".format(self.name,self.phoneNumber))
        print("info subject:{},StudentId:{}".format(self.subject,self.StudentId))

p=Person("전우치","010-222-1234")
s=Student("이순신","010-111-1234","컴공","941213")

print(p.__dict__)
print(s.__dict__)

# p.printInfo()
# s.printInfo()