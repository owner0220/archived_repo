N = int(input())


def bublesort(arr):
    for j in range(len(arr)):
        for i in range(len(arr) - 1 - j):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp


for _ in range(N):
    numlen = int(input())
    arr = list(map(int, input().split()))
    bublesort(arr)
    print("#{} ".format(_+1), end="")
    for i in range(5):
        print(arr[(numlen-1) - i], end=" ")
        print(arr[i], end=" ")
    print()



