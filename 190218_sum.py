# import sys
# sys.stdin = open("input (3).txt", 'r')
for _ in range(10):

    N = int(input())
    arr = [list(map(int, input().split())) for a in range(100)]

    updiagonal = 0
    downdiagonal = 0
    maxVal = arr[0][0]

    for i in range(len(arr)):
        rowMax = 0
        for j in range(len(arr)):
            rowMax += arr[i][j]
        if rowMax > maxVal:
            maxVal = rowMax

    # 열
    for i in range(len(arr)):
        colMax = 0
        for j in range(len(arr)):
            colMax += arr[j][i]
        if colMax > maxVal:
            maxVal = colMax

    # 왼오위 대각선
    for i in range(len(arr)):
        updiagonal += arr[i][len(arr) - i - 1]
    if updiagonal > maxVal:
        maxVal = updiagonal

    # 왼오아래  대각선
    for i in range(len(arr)):
        downdiagonal += arr[i][i]
    if downdiagonal > maxVal:
        maxVal = downdiagonal

    print("#{} {}".format(N, maxVal))


