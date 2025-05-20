# 27455: 카드캡터 한별
import sys
from heapq import heappush, heappop

inf = int(1e16)
N, V, E = map(int, input().split())
L = [0] + list(map(int, input().split()))
k = [1] + list(map(int, input().split()))
l_dist = [[[-2] * N for _ in range(N + 1)] for _ in range(N + 1)]

link = [dict() for _ in range(V + 1)]
for _ in range(E):
    s, e, d = map(int, input().split())
    link[s][e] = d

def dijk(s, e, l):
    dist = [inf] * (V + 1)
    dist[s] = 0
    q = []
    heappush(q, (0, s))
    while q:
        d, now = heappop(q)
        if dist[now] < d: continue

        if now == e:
            return d

        for next in link[now]:
            if L[next] > l: continue
            new_d = d + link[now][next]
            if new_d < dist[next]:
                dist[next] = new_d
                heappush(q, (new_d, next))
    return -1

dp = [[-1] * (1 << (N + 1)) for _ in range(N + 1)]
for i in range(1, N + 1):
    dp[i][(1 << (N + 1)) - 1] = 0

def tsp(now, visit, l):
    if dp[now][visit] == -1:
        dp[now][visit] = inf
        for next in range(1, N + 1):
            if visit & (1 << next): continue
            dist = l_dist[now][next][l]
            if dist == -2:
                dist = dijk(k[now], k[next], l)
                l_dist[now][next][l] = dist
            if dist == -1: continue
            dp[now][visit] = min(dp[now][visit], tsp(next, visit | (1 << next), l + 1) + dist)
    return dp[now][visit]

res = tsp(0, 1, 0)
if 0 < res < inf: print(res)
else: print(-1)