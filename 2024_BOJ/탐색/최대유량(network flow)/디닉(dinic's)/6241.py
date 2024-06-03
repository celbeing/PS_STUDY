# 6241: Dining
import sys
from collections import deque
input = sys.stdin.readline
n,F,D = map(int,input().split())
N = n*2
graph = [[] for _ in range(N+F+D+2)]
capa = [{} for _ in range(N+F+D+2)]
flow = [{} for _ in range(N+F+D+2)]

def connect(u,v):
    graph[u].append(v)
    graph[v].append(u)
    capa[u][v] = 1
    flow[u][v] = 0
    capa[v][u] = 0
    flow[v][u] = 0

def lv_graph():
    level = [-1]*(F+N+D+2)
    bfs = deque([0])
    level[0] = 0
    while bfs:
        now = bfs.popleft()
        for next in graph[now]:
            if level[next] == -1 and capa[now][next]-flow[now][next] > 0:
                bfs.append(next)
                level[next] = level[now] + 1
    return level

def dinic(now, cut):
    if now == F+N+D+1: return cut
    for n in range(work[now],len(graph[now])):
        next = graph[now][work[now]]
        residual = capa[now][next]-flow[now][next]
        if level[now]+1 == level[next] and residual > 0:
            f = dinic(next,1)
            if f > 0:
                flow[now][next] += 1
                flow[next][now] -= 1
                return 1
        work[now] += 1
    return 0

for cow in range(F+1,F+n+1):
    info = list(map(int,input().split()))
    f = info[0]
    d = info[1]
    connect(cow,cow+n)
    for food in info[2:f+2]: connect(food,cow)
    for drink in info[f+2:]: connect(cow+n,drink+F+N)
for food in range(1,F+1): connect(0,food)
for drink in range(F+N+1,F+N+D+1): connect(drink,F+N+D+1)

count = 0
while True:
    level = lv_graph()
    if level[-1] == -1: break

    work = [0]*(F+N+D+2)
    while True:
        f = dinic(0,1)
        if f == 0: break
        count += f

print(count)