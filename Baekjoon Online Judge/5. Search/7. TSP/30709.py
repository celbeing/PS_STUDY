# 30709: 외판원 순회 로봇
import sys
input = sys.stdin.readline
inf = 10**9
n, m, u, v = map(int, input().split())
n += 1
dist = [[inf] * n for _ in range(n)]
for _ in range(m):
    x, y, l = map(int, input().split())
    dist[x][y] = l
for k in range(1, n):
    dist[0][k] = 0
    for i in range(1, n):
        for j in range(1, n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

# dp[i][j][v] = i에서 j로 v에 포함되지 않는 곳을 거쳐 가는 최단 거리
dp = [[[inf] * (1 << n) for _ in range(n)] for _ in range(n)]

def tsp(now, dstn, visit):
    if now == dstn and visit + 1 == 1 << n:
        dp[now][dstn][visit] = 0
    elif dp[now][dstn][visit] == inf:
        for next in range(1, n):
            if visit & (1 << next) or dist[now][next] == inf: continue
            dp[now][dstn][visit] = min(dp[now][dstn][visit], tsp(next, dstn, visit | (1 << next)) + dist[now][next])
    return dp[now][dstn][visit]

for i in range(1, n):
    tsp(0, i, 1)



print()