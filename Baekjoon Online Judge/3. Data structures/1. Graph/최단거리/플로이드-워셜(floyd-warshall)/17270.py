# 17270: 연예인은 힘들어
import sys
input = sys.stdin.readline
inf = float('inf')

v, m = map(int, input().split())
graph = [[inf] * (v + 1) for _ in range(v + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)
    graph[b][a] = min(graph[b][a], c)

for k in range(1, v + 1):
    for i in range(1, v + 1):
        if k == i: continue
        for j in range(1, v + 1):
            if i == j or k == j: continue
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

j, s = map(int, input().split())
dist = inf
for i in range(1, v + 1):
    if i in (j, s):
        continue
    dist = min(dist, graph[j][i] + graph[i][s])
j_dist = inf
res = -1
for i in range(1, v + 1):
    if i == j or i == s: continue
    d = graph[j][i] + graph[i][s]
    if graph[j][i] <= graph[i][s] and dist >= d:
        if dist > d or j_dist > graph[j][i]:
            res = i
            dist = graph[j][i] + graph[i][s]
            j_dist = graph[j][i]
print(res)