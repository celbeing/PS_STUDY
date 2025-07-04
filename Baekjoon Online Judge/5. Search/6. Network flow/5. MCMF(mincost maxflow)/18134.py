# 18134: 치삼이의 대모험
import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

def link(u, v, f, c):
    capa[u][v] = f
    capa[v][u] = 0
    flow[u][v] = 0
    flow[v][u] = 0
    cost[u][v] = c
    cost[v][u] = -c

n, m = map(int, input().split())
node = n * 2 + 1
capa = [dict() for _ in range(node)]
flow = [dict() for _ in range(node)]
cost = [dict() for _ in range(node)]
for i in range(1, n + 1):
    link(i, i + n, 1, 0)
for _ in range(m):
    l, u, v = map(int, input().split())
    link(u + n, v, 1, l)
    link(v + n, u, 1, l)
h, e = map(int, input().split())
s = 0
link(0, h, 2, 0)
capa[h][h + n] += 1

res = 0
ans = 0
while 1:
    visit = [-1] * node
    is_inQ = [0] * node
    dist = [INF] * node

    spfa = deque([s])
    dist[s] = 0
    is_inQ[s] = 1

    while spfa:
        now = spfa.popleft()
        is_inQ[now] = 0

        for next in capa[now]:
            if capa[now][next] - flow[now][next] > 0 and dist[now] + cost[now][next] < dist[next]:
                dist[next] = dist[now] + cost[now][next]
                visit[next] = now

                if is_inQ[next] == 0:
                    is_inQ[next] = 1
                    spfa.append(next)

    if visit[e] == -1: break

    f = INF
    route = e
    while route != s:
        f = min(f, capa[visit[route]][route] - flow[visit[route]][route])
        route = visit[route]

    route = e
    while route != s:
        ans += f * cost[visit[route]][route]
        flow[visit[route]][route] += f
        flow[route][visit[route]] -= f
        route = visit[route]
    res += f

print(ans if res == 2 else -1)