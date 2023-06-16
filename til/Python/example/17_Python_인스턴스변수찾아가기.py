class Person:
    name ="Default Name"
p1=Person()
p2=Person()
p1.name="전우치"
print(p1.name)
print(p2.name)


#클래스에 멤버변수 추가 시 이미 만들어진 인스턴스에도
Person.title="newtitle"
print("p1 title : ",p1.title)
print("p2 title : ",p2.title)
print("Person title : ",Person.title)

p1.age=20
print("p1 age : ",p1.age)
# print("p2 age : ",p2.age) #객체에 추가한 멤버변수는 그 객체에만 추가 된다.

str="글로벌 변수입니다."
class Gstring:
    str=""
    def set(self,msg):
        self.str=msg
    def print(self):
        print(self.str)

g=Gstring()
g.set("클래스 변수입니다.")
g.print()
print(str)
