import sys
from collections import deque
inf = int(1e9)
input = sys.stdin.readline
N,M = map(int,input().split())
graph = [[]*(N+1) for _ in range(N+1)]

def dijk(t):
    bfs = deque([(1,t)])
    time = [t]*(N+1)
    while bfs:
        now,time = bfs.popleft()
        for next,dist,limit in graph[now]:
            if time[next] > t: continue
            if limit > time+dist: continue
            bfs.append((next,time+dist))
    if time[N] == t: return -1
    else: return time[N]

for _ in range(M):
    u,v,d,t = map(int,input().split())
    graph[u].append((v,d,t))
    graph[v].append((u,d,t))
    s,e = 0,