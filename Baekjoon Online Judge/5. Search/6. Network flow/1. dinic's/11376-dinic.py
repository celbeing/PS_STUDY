# 11376: 열혈강호 2
import sys
from collections import deque
input = sys.stdin.readline
N,M= map(int,input().split())
capa = [[0]*(N+M+2) for _ in range(N+M+2)]
flow = [[0]*(N+M+2) for _ in range(N+M+2)]

for i in range(1,N+1):
    task = list(map(int,input().split()))[1:]
    for j in task:
        capa[i][N+j] = 1
    capa[0][i] = 2
for i in range(N+1,N+M+1):
    capa[i][N+M+1] = 1

def lv_graph():
    bfs = deque([0])
    level = [-1]*(N+M+2)
    level[0] = 0
    while bfs:
        now = bfs.popleft()
        for next in range(N+M+2):
            if level[next] == -1 and capa[now][next]-flow[now][next] > 0:
                bfs.append(next)
                level[next] = level[now]+1
    return level

result = 0

def dinic(now,cut):
    if now == N+M+1: return cut
    for next in range(work[now],N+M+2):
        residual = capa[now][next]-flow[now][next]
        if level[now]+1 == level[next] and residual > 0:
            f = dinic(next,min(residual,cut))
            if f > 0:
                flow[now][next] += f
                flow[next][now] -= f
                return f
        work[now] += 1
    return 0

while True:
    level = lv_graph()
    if level[-1] == -1: break

    work = [0]*(N+M+2)
    while True:
        f = dinic(0,int(1e9))
        if f == 0: break
        result += f
    if result == M: break

print(result)