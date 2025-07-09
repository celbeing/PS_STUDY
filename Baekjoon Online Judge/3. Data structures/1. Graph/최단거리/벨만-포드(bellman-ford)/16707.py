# 16707: American Tour
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
edge = []
dist = [INF] * (n + 1)
visit = [0] * (n + 1)
used = [0] * (n + 1)

for _ in range(m):
    u, v, d = map(int, input().split())
    edge.append((u, v, d))
    edge.append((v, u, d))

def bellman_ford(s, t):
    dist[s] = 0
    for i in range(n - 1):
        for j in range(m * 2):
            u, v, d = edge[j]
            if dist[u] != INF and dist[u] + d < dist[v]:
                dist[v] = dist[u] + d
                visit[v] = u
                used[v] = j
    return dist[t]

res = bellman_ford(1, 2)
r = 2
while r > 1:
    u, v, d = edge[used[r]]
    edge[used[r]] = (v, u, -d)
    r = visit[r]

dist = [INF] * (n + 1)
res += bellman_ford(n, 2)
print(res)