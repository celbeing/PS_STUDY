# 11377: 열혈강호 3
import sys
from collections import deque
inf = int(1e9)
input = sys.stdin.readline

n,m,K = map(int,input().split())
N = n*2; M = m*2
graph = [[] for _ in range(N+M+3)]

# 직원: 2~n+2; 일: N+2~N+m+2
capa = [[0]*(N+M+3) for _ in range(N+M+3)]
flow = [[0]*(N+M+3) for _ in range(N+M+3)]
for i in range(2,n+2):
    capa[1][i] = 2
    capa[i][i+n] = 2
    graph[i].append(n+i)
for i in range(N+2,N+m+2):
    capa[i][i+m] = 1
    capa[i+m][N+M+2] = 1
    graph[i].append(m+i)
capa[0][1] = n+K

def bfs():
    level = [-1]*(N+M+3)
    bfs = deque([0])
    level[0] = 0
    while bfs:
        now = bfs.popleft()
        for next in graph[now]:
            if capa[now][next]-flow[now][next] > 0 and level[now]+1 == level[next]:
                bfs.append(next)
                level[now] = next
    return level

def dfs(level,now,cut):
    global result
    if now == N+M+2: return cut
    for next in range(work[now],len(graph[now])):
        residual = capa[now][next]-flow[now][next]
        if residual > 0 and level[now]+1 == level[next]:
            f = dfs(level,next,min(residual,cut))
            work[now] += 1
            if f > 0:
                flow[now][next] += f
                flow[next][now] -= f
                result += f
    return 0

for i in range(n+2,N+2):
    task = list(map(int,input().split()))
    for j in range(1,task[0]+1):
        capa[i][N+j+1] = 1
        graph[i].append(task[j])

result = 0

work = [0]*(N+M+2)
while True:
    level = bfs()
    if level[N+M+2] == -1: break
    dfs(level,0,inf)

print(result)