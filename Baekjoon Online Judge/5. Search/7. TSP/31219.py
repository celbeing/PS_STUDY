# 31219: 세계 일주
import sys
input = sys.stdin.readline
inf = 1e8

def TSP(now, visit, route):
    if dp[now][visit] == 0.0:
        dp[now][visit] = inf
        for next in range(1, n):
            if visit & 1 << next: continue
            dp[now][visit] = min(dp[now][visit], TSP(next, visit | 1 << next, route + [country[next]]) + DIST(country[now], country[next]))
    return dp[now][visit]

def DIST(p1, p2):
    return (((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2)) ** 0.5

n = int(input())
country = [tuple(map(int, input().split())) for _ in range(n)]
dp = [[0.0] * (1 << n) for _ in range(n)]
for i in range(1, n):
    dp[i][(1 << n) - 1] = DIST(country[0], country[i])

res = TSP(0, 1, [country[0]])
if res >= inf: print(-1)
else: print(res)