# 8138: Tourist Attractions
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
inf = int(1e9)
n, m, k = map(int, input().split())

def dijk(s):
    hq = []
    distance = [inf] * n
    distance[s] = 0
    heappush(hq, (0, s))
    while hq:
        d, now = heappop(hq)
        if distance[now] < d: continue
        for next in link[now]:
            new_d = d + link[now][next]
            if new_d < distance[next]:
                distance[next] = new_d
                heappush(hq, (new_d, next))

    for i in range(k + 1):
        if i == s: continue
        dist[s][i] = distance[i]
    dist[s][k + 1] = distance[-1]

    return 0

def tsp(now, visit):
    if dp[now][visit] == 0:
        dp[now][visit] = inf
        for next in range(1, k + 1):
            if visit & (1 << next): continue
            for check in cond[next]:
                if visit & 1 << check == 0: break
            else:
                dp[now][visit] = min(dp[now][visit], tsp(next, visit | (1 << next)) + dist[now][next])
    return dp[now][visit]

# 0은 n번 지점
dist = [[inf] * (k + 2) for _ in range(k + 2)]
distance = [inf] * n
link = [dict() for _ in range(n)]
cond = [[] for _ in range(k + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    u -= 1; v -= 1
    link[u][v] = w
    link[v][u] = w

for _ in range(int(input())):
    r, s = map(int, input().split())
    r -= 1; s -= 1
    cond[s].append(r)
for i in range(k + 1):
    cond[i].sort()

for i in range(k + 1):
    dijk(i)
    dist[-1][i] = dist[i][-1]

dp = [[0] * (1 << (k + 1)) for _ in range(k + 1)]
for i in range(1, k + 1):
    dp[i][(1 << (k + 1)) - 1] = dist[i][-1]

res = tsp(0, 1)
print(res)