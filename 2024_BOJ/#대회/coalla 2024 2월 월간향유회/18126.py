#18126: 너구리 구구
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
dist = [-1 for _ in range(N+1)]
for _ in range(N-1):
    A,B,C = map(int,input().split())
    graph[A].append((B,C))
    graph[B].append((A,C))

bfs = deque([1])
dist[1] = 0
far = 0
while bfs:
    now = bfs.popleft()
    for next,edge in graph[now]:
        if dist[next] >= 0: continue
        bfs.append(next)
        dist[next] = dist[now]+edge
        if dist[next] > far:
            far = dist[next]
print(far)