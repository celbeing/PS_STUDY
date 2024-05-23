# 11378: 열혈강호 4
import sys
from collections import deque
input = sys.stdin.readline
N,M,K = map(int,input().split())
T = N+M+3

def lv_graph():
    level = [-1]*T
    bfs = deque([0])
    level[0] = 0
    while bfs:
        now = bfs.popleft()
        for next in graph[now]:
            if level[next] == -1 and capa[now][next]-flow[now][next] > 0:
                bfs.append(next)
                level[next] = level[now]+1
    return level

def dinic(now,cut):
    if now == T-1: return cut
    for next in graph[now]:
        residual = capa[now][next]-flow[now][next]
        if level[now]+1 == level[next] and residual > 0:
            f = dinic(next,min(cut,residual))
            if f > 0:
                flow[now][next] += f
                flow[next][now] -= f
                return f
    return 0

graph = [[] for _ in range(T)]
capa = [{} for _ in range(T)]
flow = [{} for _ in range(T)]

graph[0].append(1)
graph[1].append(0)
capa[0][1] = K
capa[1][0] = 0
flow[0][1] = 0
flow[1][0] = 0
for u in range(2,N+2):
    graph[0].append(u)
    graph[u].append(0)
    capa[0][u] = 1
    capa[u][0] = 0
    flow[0][u] = 0
    flow[u][0] = 0
    graph[1].append(u)
    graph[u].append(1)
    capa[1][u] = K
    capa[u][1] = 0
    flow[1][u] = 0
    flow[u][1] = 0
    task = list(map(int,input().split()))[1:]
    for v in task:
        graph[u].append(v+N+1)
        graph[v+N+1].append(u)
        capa[u][v+N+1] = 1
        capa[v+N+1][u] = 0
        flow[u][v+N+1] = 0
        flow[v+N+1][u] = 0
for u in range(N+2,N+M+2):
    graph[u].append(T-1)
    graph[T-1].append(u)
    capa[u][T-1] = 1
    capa[T-1][u] = 0
    flow[u][T-1] = 0
    flow[T-1][u] = 0

result = 0
while True:
    level = lv_graph()
    if level[-1] == -1: break

    while True:
        f = dinic(0,N+K)
        if f == 0: break
        result += f
print(result)