#15591: MooTube (Silver)
import sys
from collections import deque
input = sys.stdin.readline
N, Q = map(int, input().split())
inf = 1e9
graph = [[] for _ in range(N + 1)]
for i in range(1, N):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))
    graph[q].append((p, r))
usado = [[inf for _ in range(N + 1)] for _ in range(N + 1)]
bfs = deque()
for i in range(1, N + 1):
    bfs.append(i)
    while bfs:
        now = bfs.popleft()
        for next, r in graph[now]:
            if usado[i][next] < inf: continue
            bfs.append(next)
            if usado[i][next] > r:
                usado[i][next] = r
            if usado[i][next] > usado[i][now]:
                usado[i][next] = usado[i][now]

    usado[i][i] = 0

for _ in range(Q):
    k, v = map(int, input().split())
    count = 0
    for i in range(1, N + 1):
        u = min(usado[i][v], usado[v][i])
        if u >= k:
            count += 1
    print(count)