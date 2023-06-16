value=5
while value > 0:
    print(value)
    value -=1

I=['apple',100,15.25]
for i in I:
    print(i,type(i))

d={"apple":100,"orange":200,"banana":300}

for k,v in d.items():
    print(k,v)

L=[1,2,3,4,5,6,7,8,9,10]
for i in L:
    if i>5:
        break
    print("Item :{}".format(i))

for i in L:
    if i%2==0:
        continue
    print("item :{}".format(i))