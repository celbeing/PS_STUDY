# 30975: 약간 모자라지만 착한 친구야
import sys
input = sys.stdin.readline
inf = 2_000
n, m = map(int, input().split())
dist = [[inf] * (n + 1) for _ in range(n + 1)]
p = list(map(int, input().split())) + [n]
dp = [[0] * (1 << (n + 1)) for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    dist[u - 1][v - 1] = min(dist[u - 1][v - 1], w)
for i in range(n):
    p[i] -= 1
    dp[i][(1 << (n + 1)) - 1] = dist[i][n]

def TSP(now, visit):
    if dp[now][visit] == 0:
        dp[now][visit] = inf
        for i in range(n):
            if dist[now][i] == inf or visit & 1 << i: continue
            if p[i] != i and not(visit & 1 << p[i]): continue
            dp[now][visit] = min(dp[now][visit], TSP(i, visit | 1 << i) + dist[now][i])
    return dp[now][visit]

res = TSP(n, 1 << n)
if res >= inf: print(-1)
else: print(res)