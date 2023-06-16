def divide(a,b):
    return a/b

try:
    c=divide(5,'string')
except ZeroDivisionError:
    print("인자가 0은 안되")
except TypeError:
    print("모든 인자는 숫자로!")
except :
    print("무슨 에러지?")
else :
    print("result:{}".format(c))
finally :
    print("finally 는 항상 실행된다.")
    