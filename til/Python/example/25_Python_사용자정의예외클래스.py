def raiseErrorFunc():
    raise NameError
try:
    raise ErrorFunc()
except:
    print("NameError is Catched")


class NegativeError(Exception):
    def __init__(self,value):
        self.value=value

def positiveDivide(a,b):
    if(b<0):
        raise NegativeError(b)
    return a/b

try:
    ret=positiveDivide(10,-3)
    print('10/3={}'.format(ret))
except NegativeError as e:
    print('에러값은 ',e.value)
except ZeroDivisionError as e:
    print('에러야! ',e.args[0])