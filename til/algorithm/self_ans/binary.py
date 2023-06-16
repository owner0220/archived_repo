import sys


sys.stdin = open("1.txt",'r')

def binarysearch(total, target):
    left = 0
    right = total
    cnt = 1
    while left <= right:
        middle = (left + right) // 2
        print("검색 중 지금 left",left,", middle :",middle,", right :",right)
        if target == middle:
            return cnt
        if middle > target:
            right = middle-1
        else:
            left = middle+1
        cnt+=1


    return False







def winner(a, b):
    if a==False:
        print("B")
    elif b==False:
        print("A")

    if a > b:
        print("B")
    elif a==b:
        print("0")
    else:
        print("A")


T = int(input())

for _ in range(T):
    arr = list(map(int, input().split()))
    A = binarysearch(arr[0], arr[1])

    B = binarysearch(arr[0], arr[2])
    print("#{}".format(_ + 1), end=" ")
    winner(A, B)



