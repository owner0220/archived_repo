t=(1,2,3)
print(type(t))

a,b=1,2
print(a,b)

(a,b)=(1,2)
print(a,b)

def calc(a,b):
    return a+b, a*b

x,y=calc(5,4)
print(x,y)