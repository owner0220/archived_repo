class Myclass:
    def __init__(self,value):
        self.value=value
        print("class is created! value= ",value)
    def __del__(self):
        print("class is deleted!!")

d=Myclass(10)
d_copy=d
del d
del d_copy