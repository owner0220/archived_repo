import sys
sys.stdin = open("input.txt","r")

N = int(input())

arr = [list(map(int,input().split())) for i in range(N)]

dx = [-1,0,1,0]
dy = [0,-1,0,1]
total = 0
for i in range(N):
    for j in range(N):
        for direction in range(4):
            x = i+dx[direction]
            y = j+dy[direction]
            if x < 0 or y < 0 or x >= N or y >= N:
                pass
            else:
                if arr[x][y]-arr[i][j] > 0:
                    total+=arr[x][y]-arr[i][j]
                else:
                    total-=arr[x][y]-arr[i][j]
print(total)


# 쑛코딩
# for i in range(N):
#     for j in range(N):
#         for direction in range(4):
#             x = i+dx[direction]
#             y = j+dy[direction]
#             if x < 0 or y < 0 or x >= N or y >= N:
#                 pass
#             else:
#                 total+= arr[x][y]-arr[i][j] if arr[x][y]-arr[i][j] > else total-=arr[x][y]-arr[i][j]


