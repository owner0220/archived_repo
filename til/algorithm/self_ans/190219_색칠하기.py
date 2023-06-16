T = int(input())
arrmap = []
color = []
for i in range(0, 10):
    new = []
    for j in range(0, 10):
        new.append(0)
    arrmap.append(new)


def fillcolor(arr):
    global arrmap
    global color
    for y in range(arr[1], arr[3] + 1):
        for x in range(arr[0], arr[2] + 1):
            if arrmap[y][x] == 0:
                arrmap[y][x] = arr[4]
            elif arrmap[y][x] != arr[4]:
                arrmap[y][x] += arr[4]

    if arr[4] not in color:
        color.append(arr[4])


def initmap():
    global arrmap
    global color
    for i in range(10):
        for j in range(10):
            arrmap[i][j] = 0
    for i in range(len(color)):
        color.pop()


def checkresult(i):
    result = 0
    global arrmap
    for y in range(len(arrmap)):
        for x in range(len(arrmap[0])):

            if arrmap[y][x] not in color and arrmap[y][x] != 0:
                result += 1
    print("#{}".format(i), result)


for _ in range(T):
    n = int(input())

    for a in range(n):
        fillcolor(list(map(int, input().split())))

    checkresult(_ + 1)
    initmap()







