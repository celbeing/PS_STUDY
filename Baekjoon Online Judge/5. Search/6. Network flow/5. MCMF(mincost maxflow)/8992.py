# 8992: 집기 게임
import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

def link(u, v, f = 1, c = 0):
    capa[u][v], capa[v][u] = f, 0
    flow[u][v], flow[v][u] = 0, 0
    cost[u][v], cost[v][u] = c, -c

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    node = n + m + 2
    s, t = 0, node - 1
    capa = [dict() for _ in range(node)]
    flow = [dict() for _ in range(node)]
    cost = [dict() for _ in range(node)]
    h = []
    for i in range(1, n + 1):
        link(s, i)
        h.append(tuple(map(int, input().split())))
    for j in range(n + 1, n + m + 1):
        link(j, t)
        vx, a, z, b, vw = tuple(map(int, input().split()))
        if a > b: a, b = b, a
        i = 1
        for c, hy, d, y, hw in h:
            if c > d: c, d = d, c
            if c < vx < d and a < hy < b:
                link(i, j, 1, -(vw * hw))
            i += 1

    max_flow, max_score = 0, 0
    while 1:
        visit = [-1] * node
        is_inQ = [0] * node
        dist = [INF] * node

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
                        SPFA.append(next)
                        is_inQ[next] = 1

        if visit[t] == -1: break

        f, r = INF, t
        while r != s:
            f = min(f, capa[visit[r]][r] - flow[visit[r]][r])
            r = visit[r]
        max_flow += f

        r = t
        while r != s:
            flow[visit[r]][r] += f
            flow[r][visit[r]] -= f
            max_score -= cost[visit[r]][r]
            r = visit[r]

    print(max_flow, max_score)