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
        for next, new_d in link[now]:
            new_d += d
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
        for next in range(k):
            if visit & (1 << next): continue
            for check in cond[next]:
                if visit & 1 << check == 0: break
            else:
                dp[now][visit] = min(dp[now][visit], tsp(next, visit | (1 << next)) + dist[now + 1][next + 1])
    return dp[now][visit]

# 0은 n번 지점
dist = [[inf] * (k + 2) for _ in range(k + 2)]
link = [[] for _ in range(n)]
cond = [[] for _ in range(k)]
from_start = [0] * k

for _ in range(m):
    u, v, w = map(int, input().split())
    u -= 1; v -= 1
    link[u].append((v, w))
    link[v].append((u, w))

for _ in range(int(input())):
    r, s = map(int, input().split())
    r -= 2; s -= 2
    cond[s].append(r)
for i in range(k):
    cond[i].sort()

for i in range(k + 1):
    dijk(i)
    dist[-1][i] = dist[i][-1]

for i in range(k):
    from_start[i] = dist[0][i + 1]

dp = [[0] * (1 << k) for _ in range(k)]
for i in range(k):
    dp[i][(1 << k) - 1] = dist[i + 1][-1]

res = inf
for i in range(k):
    if cond[i]: continue
    res = min(res, tsp(i, 1 << i) + from_start[i])
if res == inf:
    res = dist[0][-1]
print(res)