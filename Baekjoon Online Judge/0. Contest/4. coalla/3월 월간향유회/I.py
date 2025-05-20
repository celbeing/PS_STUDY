#16236: 아기상어
import sys
from collections import deque
input = sys.stdin.readline
d = [(1,0),(0,1),(-1,0),(0,-1)]
N = int(input())
field = [list(map(int,input().split())) for _ in range(N)]
x,y,size,ate,time = 0,0,0,0,0
for i in range(N):
    for j in range(N):
        if field[i][j] == 9:
            x = i
            y = j
            size = 2
            field[i][j] = 0
            break
    if size: break

def fish(field,a,b,size):
    field[a][b] = -1
    bfs = deque([(a,b,0)])
    caneat = []
    while bfs:
        x,y,t = bfs.popleft()
        for i in range(4):
            dx = x+d[i][0]
            dy = y+d[i][1]
            if 0<=dx<N and 0<=dy<N and field[dx][dy] <= size:
                if field[dx][dy] == 0:
                    field[dx][dy] = -10
                    bfs.append((dx,dy,t+1))
                elif field[dx][dy] == size:
                    field[dx][dy] = -size
                    bfs.append((dx,dy,t+1))
                elif 0<field[dx][dy]<size:
                    if caneat and caneat[0][0] == t:
                        caneat.sort()
                        return (caneat[0][1],caneat[0][2],caneat[0][0])
                    caneat.append((t+1,dx,dy,field[dx][dy]))
                    field[dx][dy] *= -1
    if caneat:
        caneat.sort()
        return (caneat[0][1],caneat[0][2],caneat[0][0])
    return (-1,-1,-1)

def init(field):
    for i in range(N):
        for j in range(N):
            if x == i and y == j:
                field[i][j] = 0
            elif field[i][j] == -10:
                field[i][j] = 0
            elif field[i][j] < 0:
                field[i][j] *= -1

while True:
    nx,ny,t = fish(field,x,y,size)
    if t == -1:
        break
    init(field)

    field[nx][ny] = 0
    ate += 1
    if size == ate:
        size += 1
        ate = 0
    x = nx
    y = ny
    time += t

print(time)