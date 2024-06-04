import sys
from collections import deque
input = sys.stdin.readline
D = [(1,0),(0,1),(-1,0),(0,-1)]
N,M,R,C = map(int,input().split())
rooms = [tuple(map(int,input().split())) for _ in range(R)]
dist = [[-1]*M for _ in range(N)]
bfs = deque()
for _ in range(C):
    c,d = map(int,input().split())
    bfs.append((c-1,d-1))
    dist[c-1][d-1] = 0
while bfs:
    x,y = bfs.popleft()
    for i in range(4):
        dx = x+D[i][0]
        dy = y+D[i][1]
        if 0<=dx<N and 0<=dy<M and dist[dx][dy] == -1:
            bfs.append((dx,dy))
            dist[dx][dy] = dist[x][y]+1
low = 200000
for a,b,p in rooms:
    new = dist[a-1][b-1]*p
    if low > new: low = new
print(low)