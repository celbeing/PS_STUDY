# 16991: 외판원 순회 3
import sys
input = sys.stdin.readline
inf = 50_000
n = int(input())
cord = []
dist = [[inf] * n for _ in range(n)]
for i in range(n):
    x, y = map(int, input().split())
    cord.append((x, y))
    for j in range(i):
        d = (((cord[i][0] - cord[j][0]) ** 2) + (cord[i][1] - cord[j][1]) ** 2) ** 0.5
        dist[i][j] = d
        dist[j][i] = d

dp = [[0] * (1 << n) for _ in range(n)]
for i in range(1, n):
    dp[i][(1 << n) - 1] = dist[i][0]

def TSP(now, visit):
    if dp[now][visit] == 0:
        dp[now][visit] = inf
        for i in range(n):
            if visit & 1 << i: continue
            dp[now][visit] = min(dp[now][visit], TSP(i, visit | 1 << i) + dist[now][i])
    return dp[now][visit]

res = TSP(0, 1)
print(res)