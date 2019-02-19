import sys

sys.stdin = open("input2.txt",'r')


T = input()
for _ in range(int(T)):
    knm=list(map(int,input().split()))
    golen = knm[0]
    end = knm[1]
    chargesation = knm[2]

    arr = list(map(int,input().split()))
    arr.insert(chargesation,end)
    arr.insert(0,0)

    ran=list()
    for i in range(chargesation+1):
        ran.append(arr[i+1]-arr[i])

    fuel=golen
    cnt=0
    for j in range(len(ran)-1):
        fuel = fuel - ran[j]

        if ran[j] > golen:
            cnt=0
            break

        if ran[j+1] > fuel:
            fuel = golen
            cnt+=1


    print("#{} {}".format((_ + 1), cnt))
