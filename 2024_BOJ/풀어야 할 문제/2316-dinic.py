# 2316: 도시 왕복하기 2-디닉
import sys
from collections import deque
input = sys.stdin.readline

def node(u,v,f=1):
    graph[u].append(v)
    graph[v].append(u)
    capa[u][v] = f

def lv_graph():
    level = [-1]*(N*2+1)
    level[1] = 0
    bfs = deque([1])
    while bfs:
        now = bfs.popleft()
        for next in graph[now]:
            if level[next] == -1:
                bfs.append(next)
                level[next] = level[now]+1
    return level

def dfs(level,now,cut):
    global result
    if now == 2:
        return cut
    for next in range(work[now],len(graph[now])):
        if capa[now][next]-flow[now][next] > 0 and level[next]-level[now] == 1:
            f = dfs(level,next,min(cut,capa[capa[now][next]-flow[now][next]]))
            if f > 0:
                flow[now][next] += f
                flow[next][now] -= f
                result += f
            work[now]+=1
    return 0

N,P = map(int,input().split())
graph = [[] for _ in range(N*2+1)]
capa = [[0]*(N*2+1) for _ in range(N*2+1)]
flow = [[0]*(N*2+1) for _ in range(N*2+1)]
for i in range(3,N+1):
    node(i,N+i)
node(1,N+1,P)
for _ in range(P):
    u,v = map(int,input().split())
    node(u,N+v)
    node(v,N+u)

result = 0
work = [0]*(N*2+1)
while True:
    level = lv_graph()
    if level[2] == -1: break
    dfs(level,1,P)
print(result)