# 2311: 왕복 여행
import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

def link(u, v, f, c):
    capa[u][v], capa[v][u] = f, 0
    flow[u][v], flow[v][u] = 0, 0
    cost[u][v], cost[v][u] = c, -c

n, m = map(int, input().split())
node = n + m * 2 + 2
# i = j의 연결
# i(1~n) = t(n+1~n+m) =(정점 분할, 비용 c)= t+m(n+m+1~n+m*2) = j
# source = 0, sink = -1

capa = [dict() for _ in range(node)]
flow = [dict() for _ in range(node)]
cost = [dict() for _ in range(node)]

s, e = 0, n
link(0, 1, 2, 0)
for t in range(n + 1, n + m + 1):
    a, b, c = map(int, input().split())

    link(a, t, 1, 0)
    link(b, t, 1, 0)
    link(t, t + m, 1, c)
    link(t + m, b, 1, 0)
    link(t + m, a, 1, 0)

res = 0
while 1:
    visit = [-1] * node
    is_inQ = [0] * node
    dist = [INF] * node

    spfa = deque([0])
    is_inQ[0] = 1
    dist[0] = 0
    while spfa:
        now = spfa.popleft()
        is_inQ[now] = 0
        for nxt in capa[now]:
            if capa[now][nxt] - flow[now][nxt] > 0 and dist[nxt] > dist[now] + cost[now][nxt]:
                visit[nxt] = now
                dist[nxt] = dist[now] + cost[now][nxt]
                if is_inQ[nxt] == 0:
                    spfa.append(nxt)
                    is_inQ[nxt] = 1

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
        res += cost[visit[r]][r]
        r = visit[r]

print(res)