import sys

sys.stdin = open("rsum.txt",'r')

T = int(input())

for _ in range(T):
    arr = list(map(int,input().split()))
    N = arr[0]
    M = arr[1]
    number = list(map(int,input().split()))


    temp = 0
    for x in range(M):
        temp+= number[x]
    minSum = temp
    maxSum = temp
    # print(temp)

    for i in range(len(number)-M):
        tmp=0
        for j in range(i+1,i+M+1):
            tmp+=number[j]

        if minSum > tmp:
            minSum = tmp
        if maxSum < tmp:
            maxSum = tmp
    result = maxSum-minSum
    print("#{}".format(_+1),result)
