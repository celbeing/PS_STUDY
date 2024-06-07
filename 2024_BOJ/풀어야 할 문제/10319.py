# 10319: 좀비 아포칼립스
import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def connect(u,v,k = int(1e9)):
    if v in graph[u]:
        capa[u][v] += k
    else:
        graph[u].append(v)
        capa[u][v] = k
        flow[u][v] = 0
        graph[v].append(u)
        capa[v][u] = 0
        flow[v][u] = 0

def lv_graph():
    level = [-1]*(tt+2)
    level[0] = 0
    bfs = deque([0])
    while bfs:
        now = bfs.popleft()
        for next in graph[now]:
            if level[next] == -1 and capa[now][next]-flow[now][next] > 0:
                bfs.append(next)
                level[next] = level[now]+1
    return level

def dinic(now,cut):
    if now == tt+1: return cut
    for n in range(work[now],len(graph[now])):
        next = graph[now][n]
        resid = capa[now][next]-flow[now][next]
        if level[now]+1 == level[next] and resid > 0:
            f = dinic(next,min(cut,resid))
            if f > 0:
                flow[now][next] += f
                flow[next][now] -= f
                return f
        work[now] += 1
    return 0

T = int(input())
for _ in range(T):
    n = int(input())
    tt = n*100
    i,g,s = map(int,input().split())
    m = int(input())
    graph = [[] for _ in range(tt+2)]
    capa = [{} for _ in range(tt+2)]
    flow = [{} for _ in range(tt+2)]

    for u in range(1,n+1):
        for v in range(-99,-100+s):
            connect(u*100+v,u*100+v+1)
    connect(0,i*100-99)

    for _ in range(m):
        hos = int(input())
        connect(hos*100-100+s,tt+1)

    for _ in range(int(input())):
        a,b,p,t = map(int,input().split())
        if a == i:
            connect(0,b*100-100+t,p)
        for k in range(-99,-99+s-t):
            connect(a*100+k,b*100+k+t,p)

    arrive = 0
    while True:
        level = lv_graph()
        if level[-1] == -1: break

        work = [0]*(tt+2)
        while True:
            f = dinic(0,int(1e9))
            if f == 0: break
            arrive += f
            if arrive >= g: break
        if arrive >= g: break

    print(min(g,arrive))