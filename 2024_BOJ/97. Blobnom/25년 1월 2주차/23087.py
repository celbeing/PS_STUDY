# 23087: 최단최단경로
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
def solution():
    inf = int(2e10) + 1
    mod = int(1e9) + 9
    n, m, x, y = map(int, input().split())
    metro = [dict() for _ in range(n + 1)]
    link = [[] for _ in range(n + 1)]
    dist = [inf] * (n + 1)
    trans = [int(1e5)] * (n + 1)
    before = [[] for _ in range(n + 1)]
    case = [0] * (n + 1)

    dist[x] = 0
    trans[x] = 0
    case[x] = 1

    for _ in range(m):
        u, v, w = map(int, input().split())
        metro[u][v] = w
        link[u].append(v)

    hq = [(0, 0, x)]
    while hq:
        d, t, now = heappop(hq)
        if dist[now] < d: continue
        if dist[now] == d and trans[now] < t: continue

        for befo in before[now]:
            case[now] += case[befo]
            case[now] %= mod

        for next in link[now]:
            new_dist = d + metro[now][next]
            if new_dist == dist[next]:
                if trans[now] + 1 == trans[next]:
                    before[next].append(now)
                elif trans[now] + 1 < trans[next]:
                    before[next].clear()
                    before[next].append(now)
                    trans[next] = trans[now] + 1
                    heappush(hq, (new_dist, trans[next], next))
            elif new_dist < dist[next]:
                before[next].clear()
                before[next].append(now)
                trans[next] = trans[now] + 1
                dist[next] = new_dist
                heappush(hq, (new_dist, trans[next], next))

    if dist[y] < inf:
        print(dist[y])
        print(trans[y])
        print(case[y])
    else:
        print(-1)
solution()