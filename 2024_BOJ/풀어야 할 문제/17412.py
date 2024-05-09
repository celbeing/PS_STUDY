# 17412: 도시 왕복하기 1
import sys
from collections import deque
input = sys.stdin.readline
N, P = map(int,input().split())
capa = [[0]*(N+1) for _ in range(N+1)]
flow = [[0]*(N+1) for _ in range(N+1)]

for _ in range(P):
    u,v = map(int,input().split())
    capa[u][v] += 1

result = 0

while True:
    bfs = deque([1])
    visit = [0]*(N+1)
    while bfs:
        now = bfs.popleft()
        for next in range(1,N+1):
            if capa[now][next]-flow[now][next]>0 and visit[next]==0:
                visit[next] = now
                bfs.append(next)
                if next == 2: break

    if visit[2] == 0: break

    residual = int(1e9)
    route = 2

    while route > 1:
        if residual > capa[visit[route]][route]-flow[visit[route]][route]:
            residual = capa[visit[route]][route]-flow[visit[route]][route]
        route = visit[route]

    route = 2
    while route > 1:
        flow[visit[route]][route] += residual
        flow[route][visit[route]] -= residual
        route = visit[route]

    result += residual

print(result)