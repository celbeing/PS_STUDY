# 11407: 책 구매하기 3
import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

def mcmf():
    n, m = map(int, input().split())
    node = n + m + 1

    def link(u, v, f, c):
        capa[u][v] = f
        capa[v][u] = 0
        flow[u][v] = 0
        flow[v][u] = 0
        cost[u][v] = c
        cost[v][u] = -c

    capa = [dict() for _ in range(node + 1)]
    flow = [dict() for _ in range(node + 1)]
    cost = [dict() for _ in range(node + 1)]
    a = list(map(int, input().split()))
    for i in range(1, n + 1):
        link(0, i, a[i - 1], 0)
    b = list(map(int, input().split()))
    for i in range(n + 1, node):
        link(i, node, b[i - n - 1], 0)
    for j in range(n + 1, node):
        c = list(map(int, input().split()))
        for i in range(1, n + 1):
            link(i, j, c[i - 1], 0)
    for j in range(n + 1, node):
        d = list(map(int, input().split()))
        for i in range(1, n + 1):
            link(i, j, capa[i][j], d[i - 1])

    s, e = 0, node
    min_flow = 0
    min_cost = 0
    while 1:
        visit = [-1] * (node + 1)
        is_inQ = [0] * (node + 1)
        dist = [INF] * (node + 1)

        SPFA = deque([0])
        dist[s] = 0
        is_inQ[s] = 1

        while SPFA:
            now = SPFA.popleft()
            is_inQ[now] = 0
            for next in capa[now]:
                if capa[now][next] - flow[now][next] > 0 and dist[now] + cost[now][next] < dist[next]:
                    dist[next] = dist[now] + cost[now][next]
                    visit[next] = now
                    if is_inQ[next] == 0:
                        is_inQ[next] = 1
                        SPFA.append(next)
        if visit[e] == -1: break

        f = INF
        r = e
        while r != s:
            f = min(f, capa[visit[r]][r] - flow[visit[r]][r])
            r = visit[r]

        r = e
        while r != s:
            min_cost += f * cost[visit[r]][r]
            flow[visit[r]][r] += f
            flow[r][visit[r]] -= f
            r = visit[r]

        min_flow += f
    print(min_flow)
    print(min_cost)
mcmf()