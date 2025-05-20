# 4069: Hie with the Pie
import sys
input = sys.stdin.readline
inf = int(1e9)

def tsp(now, visit):
    if dp[now][visit] == 0:
        dp[now][visit] = inf
        for next in range(1, n + 1):
            if visit & (1 << next): continue
            dp[now][visit] = min(dp[now][visit], tsp(next, visit | (1 << next)) + dist[now][next])
    return dp[now][visit]

while True:
    n = int(input())
    if n == 0: break
    dist = [list(map(int, input().split())) for _ in range(n + 1)]
    for k in range(n + 1):
        for i in range(n + 1):
            for j in range(n + 1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    dp = [[0] * (1 << (n + 1)) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][(1 << (n + 1)) - 1] = dist[i][0]

    print(tsp(0, 1))