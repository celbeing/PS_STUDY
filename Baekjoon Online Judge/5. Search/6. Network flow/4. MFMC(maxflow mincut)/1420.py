# 1420: 학교 가지마!
import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N,M = map(int,input().split())
T = N*M*2
maps = [[] for _ in range(N)]
edge = [[] for _ in range(T)]
capa = [{} for _ in range(T)]
flow = [{} for _ in range(T)]

dh = (); hg = ()
s,t = 0,0

def connect(u,v,f = 1):
    edge[u].append(v)
    edge[v].append(u)
    capa[u][v] = f
    capa[v][u] = 0
    flow[u][v] = 0
    flow[v][u] = 0

def lv_graph():
    level = [-1]*T
    level[s] = 0
    bfs = deque([s])
    while bfs:
        now = bfs.popleft()
        for next in edge[now]:
            if level[next] == -1 and capa[now][next]-flow[now][next] > 0:
                bfs.append(next)
                level[next] = level[now]+1
    return level

def dinic(now,cut):
    if now == t: return cut
    for i in range(work[now],len(edge[now])):
        next = edge[now][i]
        residual = capa[now][next]-flow[now][next]
        if level[now] + 1 == level[next] and residual > 0:
            f = dinic(next,min(cut,residual))
            if f > 0:
                flow[now][next] += f
                flow[next][now] -= f
                return f
    return 0


for i in range(N):
    maps[i] += list(input().rstrip())
    for j in range(M):
        if maps[i][j] == "K":
            dh = (i,j)
            s = (i*M+j)*2+1
        elif maps[i][j] == "H":
            hg = (i,j)
            t = (i*M+j)*2

if abs(dh[0]-hg[0])+abs(dh[1]-hg[1]) == 1 or N*M<=2:
    print(-1)
    exit()

u = 0
for i in range(N):
    for j in range(M):
        connect((i*M+j)*2,(i*M+j)*2+1)
        if i < N-1 and maps[i][j] != "#" and maps[i+1][j] != "#":
            v = u+2*M
            connect(u+1,v,int(1e9))
            connect(v+1,u,int(1e9))
        if j < M-1 and maps[i][j] != "#" and maps[i][j+1] != "#":
            v = u+2
            connect(u+1,v,int(1e9))
            connect(v+1,u,int(1e9))
        u += 2

result = 0
while True:
    level = lv_graph()
    if level[t] == -1: break

    work = [0]*T
    while True:
        f = dinic(s,int(1e9))
        if f == 0: break
        result += f
print(result)