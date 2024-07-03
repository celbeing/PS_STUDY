import sys
from collections import deque
input = sys.stdin.readline
d = [(1,0),(0,1),(-1,0),(0,-1)]

R,C = map(int,input().split())
field = [list(input().rstrip()) for _ in range(R)]
visit = [[0]*C for _ in range(R)]
sheeps = 0
wolves = 0

def bfs(i,j):
    dq = deque([(i,j)])
    s,w = 0,0
    visit[i][j] = 1
    while dq:
        x,y = dq.popleft()
        if field[x][y] == "o": s += 1
        elif field[x][y] == "v": w += 1

        for k in range(4):
            dx = x+d[k][0]
            dy = y+d[k][1]
            if 0<=dx<R and 0<=dy<C and not visit[dx][dy] and not field[dx][dy] == "#":
                visit[dx][dy] = 1
                dq.append((dx,dy))
    if s > w: return s
    else: return -w

for i in range(R):
    for j in range(C):
        if visit[i][j] or field[i][j] == "#": continue
        f = bfs(i,j)
        if f > 0: sheeps += f
        else: wolves -= f
print(sheeps,wolves)