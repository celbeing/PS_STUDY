# 2316: 도시 왕복하기 2-디닉
import sys
from collections import deque
input = sys.stdin.readline
inf = int(1e9)

def connect(u,v):
    graph[u*2].append(v*2-1)
    graph[v*2-1].append(u*2)
    graph[v*2].append(u*2-1)
    graph[u*2-1].append(v*2)
    capa[u*2][v*2-1] = 1
    flow[u*2][v*2-1] = 0
    capa[v*2-1][u*2] = 0
    flow[v*2-1][u*2] = 0
    capa[v*2][u*2-1] = 1
    flow[v*2][u*2-1] = 0
    capa[u*2-1][v*2] = 0
    flow[u*2-1][v*2] = 0

def city(i):
    graph[i].append(i+1)
    graph[i+1].append(i)
    capa[i][i+1] = 1
    capa[i+1][i] = 0
    flow[i][i+1] = 0
    flow[i+1][i] = 0

def lv_graph():
    level = [-1]*(N+1)
    bfs = deque([1])
    level[1] = 0
    while bfs:
        now = bfs.popleft()
        for next in graph[now]:
            if level[next] == -1 and capa[now][next]-flow[now][next] > 0:
                level[next] = level[now]+1
                bfs.append(next)
    return level

def dfs(now,cut):
    if now == 4: return 1

    for n in range(work[now],len(graph[now])):
        next = graph[now][n]
        residual = capa[now][next]-flow[now][next]
        if level[now]+1 == level[next] and residual > 0:
            f = dfs(next,1)
            if f > 0:
                flow[now][next] += 1
                flow[next][now] -= 1
                return f
        work[now] += 1
    return 0

n,P = map(int,input().split())
N = n*2
graph = [[] for _ in range(N+1)]
capa = [{} for _ in range(N+1)]
flow = [{} for _ in range(N+1)]

for i in range(1,N,2):
    city(i)
capa[1][2] = inf
capa[3][4] = inf
for _ in range(P):
    a,b = map(int,input().split())
    connect(a,b)

result = 0
while True:
    level = lv_graph()
    if level[4] == -1: break

    work = [0]*(N+1)
    while True:
        f = dfs(1,1)
        if f == 0: break
        result += f

print(result)