N = int(input())

map=[]
for x in range(N):
    map.append(list(map(int,input().split())))


map.sort()

movelen = [5,4,4,3,3,2,2,1,1]
xyToggle = 0
negativeCheck = 1
cnt=0
x=0
y=0
print(map[y][x])
for mlen in movelen:

    if mlen == 5:
        if cnt % 4 == 2 or cnt % 4 == 3:
            negativeCheck = -1
        else:
            negativeCheck = 1
        for dx in range(mlen-1):
            x = x + negativeCheck
            print(map[y][x])
            xyToggle = 1
        cnt += 1

        continue

    if xyToggle == 0:

        if cnt % 4 == 2 or cnt % 4 == 3:
            negativeCheck = -1
        else:
            negativeCheck = 1
        for dx in range(mlen):

            x = x + negativeCheck
            print(map[y][x])
            xyToggle = 1

        cnt += 1

    else:

        if cnt%4 == 2 or cnt%4 == 3 :
            negativeCheck = -1
        else:
            negativeCheck = 1
        for dy in range(mlen):

            y = y + negativeCheck
            print(map[y][x])
            xyToggle = 0

        cnt += 1




