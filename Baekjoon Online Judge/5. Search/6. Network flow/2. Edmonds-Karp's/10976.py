# 10976: 피난
import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

def edmonds_karp():
    n, m = map(int, input().split())
    s, e = 1, n
    capa = [[0] * (n + 1) for _ in range(n + 1)]
    flow = [[0] * (n + 1) for _ in range(n + 1)]
    edge = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        if u > v: u, v = v, u
        f = INF
        if u == 1 or v == n:
            f = 1
        capa[u][v] += f
        edge[u].append(v)
        edge[v].append(u)

    res = 0

    while 1:
        bfs = deque([s])
        visit = [-1] * (n + 1)
        visit[s] = 0
        while bfs:
            now = bfs.popleft()
            for next in edge[now]:
                if capa[now][next] - flow[now][next] > 0 and visit[next] == -1:
                    visit[next] = now
                    bfs.append(next)
                    if next == e:
                        bfs.clear()
                        break
        if visit[e] == -1: break

        f = float('inf')
        route = e
        while route != s:
            f = min(f, capa[visit[route]][route] - flow[visit[route]][route])
            route = visit[route]

        route = e
        while route != s:
            flow[visit[route]][route] += f
            flow[route][visit[route]] -= f
            route = visit[route]

        res += f
    return (res)

for _ in range(int(input())):
    print(edmonds_karp())