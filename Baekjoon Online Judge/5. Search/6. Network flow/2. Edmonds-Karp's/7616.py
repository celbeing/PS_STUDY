# 7616: 교실로 가는 길
import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

def link(u, v, f = 1):
    capa[u][v] = f
    capa[v][u] = 0
    flow[u][v] = 0
    flow[v][u] = 0

tc = 1
while True:
    k, n = map(int, input().split())
    if k == n == 0: break
    print(f'Case {tc}:')
    tc += 1

    node = n * 2 + 1
    capa = [dict() for _ in range(node)]
    flow = [dict() for _ in range(node)]
    nxt = list(map(int, input().split()))
    for j in nxt:
        link(1 + n, j)
    nxt = list(map(int, input().split()))
    for i in range(3, n + 1):
        link(i, i + n)
        nxt = list(map(int, input().split()))
        for j in nxt:
            if j == 1: continue
            link(i + n, j)
    link(1, 1 + n, k)

    arrived = 0
    route = [0] * (n + 1)
    while 1:
        visit = [0] * node
        bfs = deque([1])
        visit[1] = -1

        while bfs:
            now = bfs.popleft()
            for next in capa[now]:
                if capa[now][next] - flow[now][next] > 0 and visit[next] == 0:
                    visit[next] = now
                    bfs.append(next)
                    if next == 2:
                        bfs.clear()
                        break

        if visit[2] == 0:
            break

        f = INF
        r = 2
        while r > 1:
            f = min(f, capa[visit[r]][r] - flow[visit[r]][r])
            if r <= n: route[visit[r] - n] = r
            r = visit[r]

        r = 2
        while r > 1:
            flow[visit[r]][r] += f
            flow[r][visit[r]] -= f
            r = visit[r]
        arrived += f

    if arrived == k:
        for s in capa[1 + n]:
            if s == 1 or flow[1 + n][s] == 0: continue
            res = [1, s]
            t = route[s]
            while res[-1] != 2:
                res.append(t)
                t = route[t]
            print(*res)
    else:
        print('Impossible')
    print()