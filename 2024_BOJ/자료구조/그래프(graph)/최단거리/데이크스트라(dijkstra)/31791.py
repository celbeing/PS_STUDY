# 31791: 바이러스 공격
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
inf = int(1e9)
d = [(1,0),(0,1),(-1,0),(0,-1)]
N,M = map(int,input().split())
Tg,Tb,X,B = map(int,input().split())
virus = [[1]*M for _ in range(N)]
dist = [[inf]*M for _ in range(N)]

dijk = []

for i in range(N):
    m = list(input().rstrip())
    for j in range(M):
        if m[j] == '*':
            virus[i][j] = 0
            heappush(dijk, (0, i, j))
            dist[i][j] = 0
        elif m[j] == '#': virus[i][j] += Tb

while dijk:
    now, x, y = heappop(dijk)
    if now > Tg: break
    for k in range(4):
        dx = d[k][0] + x
        dy = d[k][1] + y
        if 0<=dx<N and 0<=dy<M:
            new = now + virus[dx][dy]
            if dist[dx][dy] > new:
                dist[dx][dy] = new
                heappush(dijk,(new,dx,dy))
safe = []
for i in range(N):
    for j in range(M):
        if dist[i][j] > Tg:
            safe.append([i+1,j+1])
if safe:
    for t in safe:
        print(*t)
else:
    print(-1)