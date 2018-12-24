def Times (a,b):
    return a*b

print(Times)
print(Times(10,10))

print(globals())

def setValue(newValue):
    x=newValue

retval =setValue(10)

print(retval)

def swap(x,y):
    return y,x


print(swap(1,2))
a,b=swap(1,2)

def intersect(prelist,postlist):
    retList=[]
    for x in prelist:
        if x in postlist and not x in retList:
            retList.append(x)
    return retList

print(intersect("HAM","SPAM"))