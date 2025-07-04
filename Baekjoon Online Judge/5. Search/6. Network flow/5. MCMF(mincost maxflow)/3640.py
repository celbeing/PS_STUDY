# 3640: 제독
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

while 1:
    try:
        v, e = map(int, input().split())
    except:
        break
    node = v * 2 + 1
    capa = [dict() for _ in range(node)]
    flow = [dict() for _ in range(node)]
    cost = [dict() for _ in range(node)]
    for i in range(1, v + 1):
        link(i, i + v)
    capa[1][v + 1] = 2
    for _ in range(e):
        a, b, c = map(int ,input().split())
        link(a + v, b, 1, c)

    res = 0
    while 1:
        visit = [-1] * node
        is_inQ = [0] * node
        dist = [INF] * node

        spfa = deque([1])
        is_inQ[1] = 1
        dist[1] = 0

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

        if visit[v] == -1: break

        f = INF
        r = v
        while r != 1:
            f = min(f, capa[visit[r]][r] - flow[visit[r]][r])
            r = visit[r]

        r = v
        while r != 1:
            res += f * cost[visit[r]][r]
            flow[visit[r]][r] += f
            flow[r][visit[r]] -= f
            r = visit[r]
    print(res)