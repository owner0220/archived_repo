class Mycalc(object):
    def __init__(self,value):
        self.value=value
        print("class is created! value= ",value)
    def __del__(self):
        print("class is deleted!!")
    @staticmethod
    def my_add(x,y):
        return x+y


a=Mycalc.my_add(5,7)
print(a)
