# 1014: 컨닝
import sys
from collections import deque
inf = int(1e9)
input = sys.stdin.readline
d = [(-1,-1),(0,-1),(1,-1),(-1,1),(0,1),(1,1)]

def connect(u,v,c):
    if u in graph:
        capa[u][v] += c
    else:
        graph[u].append(v)
        capa[u][v] = c
        flow[u][v] = 0
        graph[v].append(u)
        capa[v][u] = 0
        flow[v][u] = 0

def lv_graph():
    level = [-1]*(N*M+2)
    bfs = deque([0])
    level[0] = 0
    while bfs:
        now = bfs.popleft()
        for next in graph[now]:
            if level[next] == -1 and capa[now][next]-flow[now][next] > 0:
                level[next] = level[now] + 1
                bfs.append(next)
    return level

def dinic(now,cut):
    if now == N*M+1: return cut

    for i in range(work[now],len(graph[now])):
        next = graph[now][i]
        residual = capa[now][next] - flow[now][next]
        if level[now]+1 == level[next] and residual > 0:
            f = dinic(next,min(residual,cut))
            if f > 0:
                flow[now][next] += f
                flow[next][now] -= f
                return f
        work[now] += 1
    return 0

C = int(input())
for _ in range(C):
    result = 0
    N,M = map(int,input().split())
    room = [list(input().rstrip()) for _ in range(N)]
    seat = 0
    for i in range(N):
        for j in range(M):
            if room[i][j] == '.': seat += 1
    graph = [[] for _ in range(N*M+2)]
    capa = [{} for _ in range(N*M+2)]
    flow = [{} for _ in range(N*M+2)]
    for i in range(N):
        for j in range(0,M,2):
            if room[i][j] == '.':
                connect(0,i*M+j+1,1)
                for k in range(6):
                    di,dj = d[k][0]+i,d[k][1]+j
                    if 0<=di<N and 0<=dj<M and room[di][dj] == '.':
                        connect(di*M+dj+1,N*M+1,1)
                        connect(i*M+j+1,di*M+dj+1,inf)

    while True:
        level = lv_graph()
        if level[-1] == -1: break
        work = [0]*(N*M+2)

        while True:
            f = dinic(0,inf)
            if f == 0: break
            result += f

    print(seat-result)