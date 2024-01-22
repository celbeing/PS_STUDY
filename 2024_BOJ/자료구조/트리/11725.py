#11725: 트리의 부모 찾기
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
parent = [-1]*(N+1)
graph = [[] for _ in range(N+1)]
for i in range(1,N):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
bfs = deque()
bfs.append(1)
parent[1] = 0
while bfs:
    now = bfs.popleft()
    for next in graph[now]:
        if parent[next] == -1:
            parent[next] = now
            bfs.append(next)
for i in range(2,N+1):
    print(parent[i])