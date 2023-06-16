x=1
def func(a):
    return a+x
print(func(1))

def func2(a):
    x=2
    return a+x

print(func2(1))

g=1
def testScope(a):
    global g
    g=2
    return g+a

print(testScope(1))
print(g)

def Times(a=10,b=20):
    return a*b

print(Times())
print(Times(5))

def connectURI(server,port):
    str="http://"+server+":"+port
    return str

print(connectURI("test.com","8080"))
print(connectURI(port="8080",server="test.com"))

def test(*args):
    print(type(args))

test(2,1)

def union(*ar):
    res=[]
    for item in ar:
        for x in item:
            if not x in res:
                res.append(x)
    return res

print(union("HAM","EGG","SPAM"))
print(union("girl","generation","gee"))

def UserURIBuilder(server,port,**user):
    str="http://"+server+":"+port+"/?"
    for key in user.keys():
        str+=key+"="+user[key]+"&"
    return str

print(UserURIBuilder("test.com","8080",id='userid',passws='1234',name='mike'))