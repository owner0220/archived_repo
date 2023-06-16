g=lambda x,y: x*y
print(g(2,3))

print((lambda x : x*x)(3))

print(globals())



for element in [1,2,3]:
    print(element)

for element in (1,2,3):
    print(element)

for key in {'one':1, 'two':2}:
    print(key)

for char in "123":
    print(char)

s='abc'
it = iter(s)
print(it)
print(next(it))

def add(a,b):
    return a+b

add.__doc__="이 함수는 2개 인자를 받아 덧셈을 하는 함수 입니다."
help(add)


#무한루프 벗어날땐 'ctrl'과 'c'를 누르면 된다.
while True:
    pass