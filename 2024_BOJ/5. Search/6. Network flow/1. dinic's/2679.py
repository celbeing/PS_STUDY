# 2679: 맨체스터의 도로
import sys
from collections import deque
from heapq import heappush, heappop
input = sys.stdin.readline

def connect(u,v,f):
    if v in graph[u]:
        capa[u][v] += f
    else:
        graph[u].append(v)
        capa[u][v] = f
        flow[u][v] = 0
        graph[v].append(u)
        capa[v][u] = 0
        flow[v][u] = 0

def lv_graph(a):
    level = [-1]*N
    level[a] = 0
    bfs = deque([a])
    while bfs:
        now = bfs.popleft()
        for next in graph[now]:
            if level[next] == -1 and capa[now][next]-flow[now][next] > 0:
                bfs.append(next)
                level[next] = level[now]+1
    return level

def dinic(now,cut):
    if now == B: return cut
    for n in range(work[now],len(graph[now])):
        next = graph[now][n]
        residual = capa[now][next]-flow[now][next]
        if level[now]+1 == level[next] and residual > 0:
            f = dinic(next,min(residual,cut))
            if f > 0:
                flow[now][next] += f
                flow[next][now] -= f
                return f
        work[now] += 1
    return 0

def dijk():
    h = []
    heappush(h,(-int(1e9),A))
    c = [0]*N
    while h:
        c_now, now = heappop(h)
        if c[now] < c_now: continue
        for next in graph[now]:
            c_next = -capa[now][next]
            if c[next] > max(c_now,c_next):
                c[next] = max(c_now,c_next)
                heappush(h,(c[next],next))
    return c

T = int(input())
for _ in range(T):
    N,E,A,B = map(int,input().split())
    graph = [[] for _ in range(N)]
    capa = [{} for _ in range(N)]
    flow = [{} for _ in range(N)]
    for _ in range(E):
        u,v,w = map(int,input().split())
        connect(u,v,w)

    maxflow = 0
    while True:
        level = lv_graph(A)
        if level[B] == -1: break

        work = [0]*N
        while True:
            f = dinic(A,int(1e9))
            if f == 0: break
            maxflow += f

    rate = dijk()
    max_rate = maxflow/-rate[B]
    print("{:.3f}".format(max_rate))