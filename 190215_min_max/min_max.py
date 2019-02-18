import sys

# with open("input.txt",'r') as txt:
#     sys.stdin = txt
sys.stdin = open("input.txt",'r')



T = input()
for _ in range(int(T)):
    arrlen = int(input())
    arr = list(map(int,input().split()))
    #버블 정렬 후에 큰 - 작
    for i in range(arrlen-1):
        for j in range(arrlen-i-1):
            if arr[j] > arr[j+1]:
                tmp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = tmp
    result = arr[arrlen-1]-arr[0]
    print("#{} {}".format((_+1),result))




