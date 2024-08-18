#1939: 중량제한
import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
graph = [{} for _ in range(N+1)]
for _ in range(M):
    u,v,l = map(int,input().split())
    if graph[u].get(v,0) < l:
        graph[u][v] = l
        graph[v][u] = l
s,e = map(int,input().split())

def dijk(w):
    visit = [0]*(N+1)
    visit[s] = 1
    bfs = deque([s])
    while bfs:
        now = bfs.popleft()
        if now == e: return True
        for next in graph[now]:
            if graph[now][next] < w: continue
            if visit[next]: continue
            visit[next] = 1
            bfs.append(next)
    return False

l,r = 0,1000000001
while l < r-1:
    m = (l+r)//2
    if dijk(m):
        l = m
    else:
        r = m
while dijk(l): l += 1
print(l-1)