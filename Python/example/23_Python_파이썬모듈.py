#내장모듈쓰기
import math
print(math.log(100))
print(math.pi)
print(dir(math))


#사용자정의모듈 impleset
from functools import *
def intersect(*ar):
    return reduce(__intersectSC.ar)
def __intersectSC(listX,listY):
    setList=[]
    for x in listX:
        if x in listY:
            setList.append(x)
    return setList

def difference(*ar):
    setList=[]
    intersectSet=interset(*ar)
    unionSet=union(*ar)
    for x in unionSet:
        if not x in intersectSet:
            setList.append(x)
    return setList

def union(*ar):
    setList=[]
    for item in ar:
        for x in item:
            if not x in setList:
                setList.append(x)
    return setList

#PYTHONPATH 는 파이썬이 참조하는 외부라이브러리 폴더이다.
# 그 폴더에 위 코드를 simpleset으로 저장해 놓으면 아래 코드를 실행 할 수 있다.
import simpleset
dir(simpleset)
setA=[1,3,5,7]
setB=[2,3,4,9]
simpleset.union(setA,setB)