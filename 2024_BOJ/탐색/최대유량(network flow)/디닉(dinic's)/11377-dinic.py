# 11377: 열혈강호 3
import sys
from collections import deque
input = sys.stdin.readline

N,M,K = map(int,input().split())
T = N*2+M+1
graph = [[] for _ in range(T+1)]
capa = [[0]*(T+1) for _ in range(T+1)]
flow = [[0]*(T+1) for _ in range(T+1)]
graph[0] = [i for i in range(1,N*2+1)]
for i in range(1,N+1):
    capa[0][i] = 1
    capa[0][i+N] = 1
    task = list(map(int,input().split()))
    for j in range(1,task[0]+1):
        graph[i].append(N*2+task[j])
        graph[i+N].append(N*2+task[j])
        capa[i][N*2+task[j]] = 1
        capa[i+N][N*2+task[j]] = 1
for i in range(N*2+1,T):
    graph[i].append(T)
    capa[i][T] = 1

def lv_graph(phase=0):
    level = [-1]*(T+1)
    level[0] = 0
    bfs = deque()
    if phase:
        for i in range(1,N+1):
            if capa[0][i]-flow[0][i] > 0:
                level[i] = 1
                bfs.append(i)
    else:
        for i in range(N+1,N*2+1):
            if capa[0][i]-flow[0][i] > 0:
                level[i] = 1
                bfs.append(i)
    while bfs:
        now = bfs.popleft()
        for next in range(N*2+M+2):
            if level[next] == -1 and capa[now][next]-flow[now][next] > 0:
                bfs.append(next)
                level[next] = level[now]+1
    return level

def dinic(now,cut):
    if now == T: return cut

    for next in range(work[now],N*2+M+2):
        residual = capa[now][next]-flow[now][next]
        if level[now]+1 == level[next] and residual > 0:
            f = dinic(next,min(cut,residual))
            if f > 0:
                flow[now][next] += f
                flow[next][now] -= f
                return f
        work[now] += 1
    return 0

result = 0

count = 0
while count < N:
    level = lv_graph(1)
    if level[-1] == -1: break

    work = [0]*T
    while True:
        f = dinic(0,int(1e9))
        if f == 0: break
        count += f
        if count == N: break

result += count
count = 0

while count < K:
    level = lv_graph()
    if level[-1] == -1: break

    work = [0]*T
    while True:
        f = dinic(0,int(1e9))
        if f == 0: break
        count += f
        if count == K: break

result += count

print(result)