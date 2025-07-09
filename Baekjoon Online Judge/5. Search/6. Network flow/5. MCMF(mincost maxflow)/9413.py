# 9413: 제주도 관광
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

for _ in range(int(input())):
    n, m = map(int, input().split())
    capa = [dict() for _ in range(n * 2 + 3)]
    flow = [dict() for _ in range(n * 2 + 3)]
    cost = [dict() for _ in range(n * 2 + 3)]
    s, t = n * 2 + 1, 0
    for i in range(1, n + 1):
        link(s, i)
        link(i, i + n, 1, -1)
        link(i + n, t)
    s += 1
    link(s, s - 1, 2)
    for _ in range(m):
        u, v = map(int, input().split())
        link(u + n, v)

    res = 0
    while 1:
        visit = [-1] * (n * 2 + 3)
        is_inQ = [0] * (n * 2 + 3)
        dist = [INF] * (n * 2 + 3)
        SPFA = deque([s])
        is_inQ[s] = 1
        dist[s] = 0
        while SPFA:
            now = SPFA.popleft()
            is_inQ[now] = 0
            for next in capa[now]:
                if capa[now][next] - flow[now][next] > 0 and dist[next] > dist[now] + cost[now][next]:
                    dist[next] = dist[now] + cost[now][next]
                    visit[next] = now
                    if is_inQ[next] == 0:
                        is_inQ[next] = 1
                        SPFA.append(next)

        if visit[t] == -1: break

        f, r = INF, t
        while r != s:
            f = min(f, capa[visit[r]][r] - flow[visit[r]][r])
            r = visit[r]

        r = t
        while r != s:
            flow[visit[r]][r] += f
            flow[r][visit[r]] -= f
            res -= cost[visit[r]][r]
            r = visit[r]

    print(res)