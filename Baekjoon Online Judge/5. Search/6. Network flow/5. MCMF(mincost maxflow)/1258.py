# 1258: 문제 할당
import sys
from collections import deque
input = sys.stdin.readline
inf = int(1e9)
N = int(input())
C = [list(map(int,input().split())) for _ in range(N)]
graph = [[] for _ in range(N*2+2)]
capa = [{} for _ in range(N*2+2)]
flow = [{} for _ in range(N*2+2)]
cost = [{} for _ in range(N*2+2)]

def connect(u,v,c = 0):
    graph[u].append(v)
    capa[u][v] = 1
    flow[u][v] = 0
    cost[u][v] = c
    graph[v].append(u)
    capa[v][u] = 0
    flow[v][u] = 0
    cost[v][u] = -c

for i in range(1,N+1):
    connect(0,i)
    connect(i+N,N*2+1)
    for j in range(1,N+1):
        connect(i,j+N,C[i-1][j-1])

result = 0
while True:
    route = [-1]*(N*2+2)
    dist = [inf]*(N*2+2)
    inQ = [False]*(N*2+2)
    Q = deque([0])
    dist[0] = 0
    inQ[0] = True
    while Q:
        now = Q.popleft()
        inQ[now] = False
        for next in graph[now]:
            residual = capa[now][next]-flow[now][next]
            new_dist = dist[now]+cost[now][next]
            if residual > 0 and dist[next] > new_dist:
                dist[next] = new_dist
                route[next] = now
                if not inQ[next]:
                    Q.append(next)
                    inQ[next] = True
    if route[-1] == -1: break

    f = inf
    now = N*2+1
    while now > 0:
        nf = capa[route[now]][now]-flow[route[now]][now]
        if f > nf: f = nf
        now = route[now]

    now = N*2+1
    while now > 0:
        result += cost[route[now]][now]*f
        flow[route[now]][now] += f
        flow[now][route[now]] -= f
        now = route[now]

print(result)