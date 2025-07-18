# 2367: 파티
import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

def link(u, v, f):
    capa[u][v], capa[v][u] = f, 0
    flow[u][v], flow[v][u] = 0, 0

n, k, d = map(int, input().split())
limit = list(map(int, input().split()))
node = n + d + 2
s, e = 0, node - 1

capa = [dict() for _ in range(node)]
flow = [dict() for _ in range(node)]

for i in range(1, n + 1):
    link(s, i, k)
for i in range(n + 1, e):
    link(i, e, limit[i - n - 1])
for i in range(1, n + 1):
    z = list(map(int, input().split()))
    for j in z[1:]:
        link(i, j + n, 1)

res = 0
while 1:
    visit = [-1] * node

    bfs = deque([0])
    while bfs:
        now = bfs.popleft()
        for nxt in capa[now]:
            if capa[now][nxt] - flow[now][nxt] > 0 and visit[nxt] == -1:
                visit[nxt] = now
                bfs.append(nxt)
                if nxt == e:
                    bfs.clear()
                    break

    if visit[e] == -1: break

    f = INF
    r = e
    while r:
        f = min(f, capa[visit[r]][r] - flow[visit[r]][r])
        r = visit[r]

    r = e
    while r:
        flow[visit[r]][r] += f
        flow[r][visit[r]] -= f
        r = visit[r]

    res += f
print(res)