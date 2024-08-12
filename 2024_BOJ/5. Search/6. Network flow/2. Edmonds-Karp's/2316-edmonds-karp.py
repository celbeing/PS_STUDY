# 2316: 도시 왕복하기 2-에드몬즈-카프
import sys
from collections import deque
inf = int(1e9)
input = sys.stdin.readline
N,P = map(int,input().split())
capa = [[0]*(N*2+1) for _ in range(N*2+1)]
flow = [[0]*(N*2+1) for _ in range(N*2+1)]
capa[1][N+1] = inf
capa[2][N+2] = inf
for i in range(3,N+1):
    capa[i][i+N] = 1
for _ in range(P):
    u,v = map(int,input().split())
    capa[u+N][v] = 1
    capa[v+N][u] = 1

result = 0

while True:
    bfs = deque([1])
    visit = [0]*(N*2+1)
    while bfs:
        now = bfs.popleft()
        for next in range(1,N*2+1):
            if visit[next] == 0 and capa[now][next]-flow[now][next] > 0:
                bfs.append(next)
                visit[next] = now
                if next == 2: break
    if visit[2] == 0: break

    residual = inf
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