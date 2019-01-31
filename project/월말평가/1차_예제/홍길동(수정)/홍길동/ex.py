# 파일명 변경 금지
# 아래에 클래스 Point와 Circle을 선언하세요.
class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Circle():
    def __init__(self,center,r):
        self.center=center
        self.r=r
    
    def get_area(self):
        pi=3.14
        return self.r**2*pi

    def get_perimeter(self):
        pi=3.14
        return 2*self.r*pi

    def get_center(self):
        return (self.center.x,self.center.y)

    def print(self):
        print("Circle: ",Circle.get_center(self)," r: ",self.r)





# 아래의 코드는 수정하지마세요. 
p1 = Point(0, 0)
c1 = Circle(p1, 3)
print(c1.get_area())
print(c1.get_perimeter())
print(c1.get_center())
c1.print()
p2 = Point(4, 5)
c2 = Circle(p2, 1)
print(c2.get_area())
print(c2.get_perimeter())
print(c2.get_center())
c2.print()