#range 수열 함수는 꼭 끝 번호는 포함하지 않는다는 것을 기억하자.
print(list(range(10)))
print(list(range(5,10)))
print(list(range(10,0,-1)))
print(list(range(10,20,2)))

I=[1,2,3,4,5]
j=[i**2 for i in I]
print(j)

t=("apple","banana","orange")

d=[len(i) for i in t]
print(d)


d={100:"apple",200:"banana",300:"orange"}
e=[v.upper() for v in d.values()]
print(e)


L=[10,25,30]
IterL=filter(None,L)
for i in IterL:
    print("Item:{}".format(i))

def GetBiggerThen20(i):
    return i>20

#필터는 True False가 확실하게 나와야 한다.
L=[10,25,30]
IterL=filter(GetBiggerThen20,L)
for i in IterL:
    print("Item:{}".format(i))