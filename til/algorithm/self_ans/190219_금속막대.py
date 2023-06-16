N = int(input())

for _ in range(N):
    n = int(input())
    check=[0]*n
    nasa = {}
    arrTmp=list(map(int,input().split()))
    for item in range(n):
        nasa[arrTmp[item*2]]=arrTmp[item*2+1]
    print("#{}".format(_+1),end=" ")
    hdktmp=0
    for x in nasa.keys():
        if x not in nasa.values():
            hdktmp = x

    for y in nasa.keys():
        print(hdktmp,nasa[hdktmp], end=" ")
        hdktmp = nasa[hdktmp]
    print()





