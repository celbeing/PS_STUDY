# 11405: 책 구매하기
import sys
from collections import deque
input = sys.stdin.readline
inf = int(1e9)

def connect(u,v,c = inf,co = 0):
    graph[u].append(v)
    capa[u][v] = c
    flow[u][v] = 0
    cost[u][v] = co
    graph[v].append(u)
    capa[v][u] = 0
    flow[v][u] = 0
    cost[v][u] = -co

N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = [list(map(int,input().split())) for _ in range(M)]

graph = [[] for _ in range(N+M+2)]
capa = [{} for _ in range(N+M+2)]
flow = [{} for _ in range(N+M+2)]
cost = [{} for _ in range(N+M+2)]
for i in range(1,N+1):
    connect(0,i,A[i-1])
    for j in range(1,M+1):
        connect(i,j+N,inf,C[j-1][i-1])
for i in range(N+1,N+M+1): connect(i,N+M+1,B[i-N-1])

result = 0
while True:
    rout = [-1]*(N+M+2)
    dist = [inf]*(N+M+2)
    inqu = [False]*(N+M+2)
    Q = deque([0])
    dist[0] = 0
    inqu[0] = True

    while Q:
        now = Q.popleft()
        inqu[now] = False
        for next in graph[now]:
            residual = capa[now][next] - flow[now][next]
            new_dist = dist[now] + cost[now][next]
            if residual > 0 and dist[next] > new_dist:
                dist[next] = new_dist
                rout[next] = now
                if not inqu[next]:
                    Q.append(next)
                    inqu[next] = True

    if rout[-1] == -1: break

    f = inf
    now = N+M+1
    while now > 0:
        if f > capa[rout[now]][now] - flow[rout[now]][now]:
            f = capa[rout[now]][now] - flow[rout[now]][now]
        now = rout[now]

    now = N+M+1
    while now > 0:
        result += f*cost[rout[now]][now]
        flow[rout[now]][now] += f
        flow[now][rout[now]] -= f
        now = rout[now]

print(result)