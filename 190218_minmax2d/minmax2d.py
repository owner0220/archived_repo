import sys
sys.stdin=open("input.txt",'r')
N=int(input())
arr = [list(map(int,input().split())) for i in range(N)]
b = [[0]*5 for i in range(5)]

maxV=arr[0][0]
minV=arr[0][0]

minX=0
minY=0
maxX=0
maxY=0

for i in range(len(arr[0])):
    for j in range(len(arr)):
        if arr[i][j] > maxV:
            maxV = arr[i][j]
            maxX = i
            maxY = j
        if arr[i][j] < minV:
            minV = arr[i][j]
            minX = i
            minY = j
print(maxV,maxX,maxY)
print(minV,minX,minY)