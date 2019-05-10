import socket
import time
import math

# User and Game Server Information
NICKNAME = '파이썬'
HOST = '127.0.0.1'
PORT = 1447 # Do not modify

# predefined variables(Do not modify these values)
TABLE_WIDTH = 254
TABLE_HEIGHT = 124
NUMBER_OF_BALLS = 5
HOLES = [ [0, 0], [130, 0], [260, 0], [0, 130], [130, 130], [260, 130] ]

class Conn:
    def __init__(self):
        self.sock = socket.socket()
        print('Trying to Connect: ' + HOST + ':' + str(PORT))
        self.sock.connect((HOST, PORT))
        print('Connected: ' + HOST + ':' + str(PORT))
        send_data = '9901/' + NICKNAME
        self.sock.send(send_data.encode('utf-8'))
        print('Ready to play.\n--------------------')
    def request(self):
        self.sock.send('9902/9902'.encode())
        print('Received Data has been currupted, Resend Requested.')
    def receive(self):
        recv_data = (self.sock.recv(1024)).decode()
        print('Data Received: ' + recv_data)
        return recv_data
    def send(self, angle, power):
        merged_data = '%d/%d' % (angle, power)
        self.sock.send(merged_data.encode('utf-8'))
        print('Data Sent: ' + merged_data)
    def close(self):
        self.sock.close()

class GameData:
    def __init__(self):
        self.reset()
    def reset(self):
        self.balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]
    def read(self, conn):
        recv_data = conn.receive()
        split_data = recv_data.split('/')
        idx = 0
        try:
            for i in range(NUMBER_OF_BALLS):
                for j in range(2):
                    self.balls[i][j] = int(split_data[idx])
                    idx += 1
        except:
            self.reset()
            conn.request()
            self.read(conn)
    def show(self):
        print('=== Arrays ===')
        for i in range(NUMBER_OF_BALLS):
            print('Ball%d: %d, %d' % (i, self.balls[i][0], self.balls[i][1]))
        print()

# 자신의 차례가 되어 게임을 진행해야 할 때 호출되는 Method
def play(conn, gameData):


    goal = [(3,124),(124,124),(254,124),(3,3),(254,3),(124,3)]

    def calcdistance(p1,p2):
        return math.pow((math.pow((p1[0]-p2[0]),2)+math.pow((p1[1]-p2[1]),2)),0.5)

    # 두점 사이거리가 제일 짧은 녀석과 그거리를 찾아줌
    def findMinpoint(p1,points):
        dis = 10000
        gp = []
        for g in points:
            if g != [0,0]:
                tmp = calcdistance(p1,g)
                if tmp < dis:
                    dis = tmp
                    gp=g
        return (gp,dis)

    def ceta1(p1,p2):
        if p2[0]-p1[0] == 0:
            if (p2[1]-p1[1]) >= 0:
                return 3
            else:
                return 183
        # print("세타1들어가기전",(p2[1] - p1[1]) / (p2[0] - p1[0]))
        # print("세타1",math.atan(((p2[1] - p1[1]) / (p2[0] - p1[0]))))
        return math.atan((abs((p2[1]-p1[1]))/abs((p2[0]-p1[0]))))*57.2958

    def ceta2(a,d,b,b2r):
        # print("a,d,b,b2r",a,d,b,b2r)
        a22 = math.pow(a,2)
        d22 = math.pow(d,2)
        b2r22 = math.pow(b2r,2)
        ad2 = 2*a*d
        print(a22,d22,b2r22,ad2)
        result = (a22+d22-b2r22)/ad2
        print("세타2",result)
        return math.acos(result)*57.2958

    def findceta(wb,goal,a,d,b,b2r):


        a = ceta2(a, d, b, b2r)
        b = ceta1(wb, goal)
        print(a,b)
        return a+b

    point1=list()
    c=0
    wb = gameData.balls[0]
    # #1. 흰 공과 목적구를 찾아간다.
    for p in gameData.balls[1:]:
        if p != [0,0]:
            point1 = p
            c = calcdistance(wb,point1)
            break

    print(point1)
    # #2. 목적구와 가장 가까운 위치의 구멍을 찾는다.
    goalpoint,b = findMinpoint(point1,goal)
    print("넣을 홀 :",goalpoint)
    print("목적구 위치:",point1)
    print("흰공위치:",wb)
    
    #1사분면에 있을때
    if point1[0] <= wb[0] and point1[1] >= wb[1]:
        print("1사분면에 있다.",ceta1(wb, point1))
        tmp = ceta1(wb, point1)
        if tmp == 3 or tmp == 183:
            angle = tmp
        else:
            angle = 270 + (tmp) + 2
    # 2사분면에 있을때
    elif point1[0] >= wb[0] and point1[1] >= wb[1]:
        print("2사분면에 있다.",ceta1(wb, point1))
        tmp = ceta1(wb, point1)
        if tmp == 3 or tmp == 183:
            angle = tmp
        else:
            angle = 90 - (tmp) + 2

    # 3사분면에 있을때
    elif point1[0] <= wb[0] and point1[1] <= wb[1]:
        print("3사분면에 있다.",ceta1(wb, point1))
        tmp = ceta1(wb, point1)
        if tmp == 3 or tmp == 183:
            angle = tmp
        else:
            angle = 270 - (tmp) + 2

    # 4사분면에 있을때
    elif point1[0] >= wb[0] and point1[1] <= wb[1]:
        print("4사분면에 있다.",ceta1(wb, point1))
        tmp = ceta1(wb, point1)
        if tmp == 3 or tmp == 183:
            angle = tmp
        else:
            angle = 90 + (tmp) + 2



    print("찾은 각도:",angle)
    power = 0
    if calcdistance(wb,goalpoint) <= calcdistance(goalpoint,point1):
        power = calcdistance(wb,goalpoint) * 1.7
        print("쎈",power)
    else:
        power = calcdistance(wb, goalpoint) * 0.58
        print("약", power)



    #
    # wb = gameData.balls[0]
    # #1. 흰 공과 가장 가까운 목적구를 찾는다.
    # point1,c = findMinpoint(gameData.balls[0],gameData.balls[1:])
    # print("목적구 위치와 흰공과 거리",point1,c)
    # print("확인",calcdistance(wb,point1))
    # #2. 목적구와 가장 가까운 위치의 구멍을 찾는다.
    # goalpoint,b = findMinpoint(point1,goal)
    # print("구멍의 위치",goalpoint,"목적구 위치",point1)
    # b = int(b)
    # c = int(c)
    # b2r = b+7.5
    # b2r = int(b2r)
    # a = int(calcdistance(gameData.balls[0],goalpoint))
    # a22 = math.pow(a,2)
    # b22 = math.pow(b,2)
    # c22 = math.pow(c,2)
    # ab2 = 2*a*b
    #
    # # print(a22+b22-c22,ab2)
    # # print((a22+b22-c22)/ab2)
    # # print(a22)
    # cosC = (a22+b22-c22)/ab2
    # print("cosC",cosC)
    # sinC = (1-cosC**2)**0.5
    # d = ((a*sinC)**2+((b2r)-a*cosC)**2)**0.5
    # d = int(d)
    # print(a,b,c,cosC,sinC,d,b2r)
    #
    # angle = findceta(wb,goalpoint,a,d,b,b2r)

    print(gameData.balls)


    ######################################################################################
    # 주어진 정보를 바탕으로 샷을 할 방향과 세기를 결정해서 angle, power 값으로 지정 #
    ######################################################################################
    conn.send(angle, power)


def main():
    conn = Conn()
    gameData = GameData()
    while True:
        gameData.read(conn)
        gameData.show()
        play(conn, gameData)        
    conn.close()
    print('Connection Closed')

if __name__ == '__main__':
    main()

