# 22870: 산책 (large)
import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

def link(u, v, f = 1, c = 0):
    capa[u][v] = f
    capa[v][u] = 0
    flow[u][v] = 0
    flow[v][u] = 0
    cost[u][v] = c
    cost[v][u] = -c

n, m = map(int, input().split())
capa = [dict() for _ in range(n * 2)]
flow = [dict() for _ in range(n * 2)]
cost = [dict() for _ in range(n * 2)]

for i in range(0, n * 2, 2):
    link(i, i + 1, 1, 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1; b -= 1
    a <<= 1; b <<= 1
    link(a + 1, b, 1, c)
    link(b + 1, a, 1, c)

s, e = map(int, input().split())
s -= 1; e -= 1
s <<= 1; e <<= 1
capa[s][s + 1] = 2
link(e, e + 1, INF)

if e in capa[s + 1]:
    print(2)
    exit()

res = 0
while 1:
    visit = [-1] * (n * 2)
    is_inQ = [0] * (n * 2)
    dist = [INF] * (n * 2)
    SPFA = deque([s])
    is_inQ[s] = 1
    dist[s] = 0
    while SPFA:
        now = SPFA.popleft()
        is_inQ[now] = 0
        for nxt in capa[now]:
            if capa[now][nxt] - flow[now][nxt] > 0 and dist[nxt] > dist[now] + cost[now][nxt]:
                dist[nxt] = dist[now] + cost[now][nxt]
                visit[nxt] = now
                if is_inQ[nxt] == 0:
                    is_inQ[nxt] = 1
                    SPFA.append(nxt)

    if visit[e + 1] == -1: break

    f, r = INF, e + 1
    while r != s:
        f = min(f, capa[visit[r]][r] - flow[visit[r]][r])
        r = visit[r]

    r = e + 1
    while r != s:
        flow[visit[r]][r] += f
        flow[r][visit[r]] -= f
        res += cost[visit[r]][r]
        r = visit[r]

print(res)