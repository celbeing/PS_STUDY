# 7734: Vista 0
import sys
input = sys.stdin.readline
inf = 1e9

def distance(p1, p2):
    return (((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2)) ** 0.5

n = int(input())
dist = [[0.0] * n for _ in range(n)]
computer = []
for i in range(n):
    computer.append(tuple(map(int, input().split())))
    dist[i][i] = inf
    for j in range(i):
        d = distance(computer[i], computer[j])
        dist[i][j] = d
        dist[j][i] = d
dp = [[0.0] * (1 << n) for _ in range(n)]
for i in range(1, n):
    dp[i][(1 << n) - 1] = dist[i][0]

route = [[-1] * (1 << n) for _ in range(n)]

def tsp(now, visit):
    if dp[now][visit] == 0:
        dp[now][visit] = inf
        for next in range(1, n):
            if visit & (1 << next): continue
            k = tsp(next, visit | 1 << next) + dist[now][next]
            if dp[now][visit] > k:
                dp[now][visit] = k
                route[now][visit] = next
    return dp[now][visit]

tsp(0, 1)
res = [0]
visit = 1
for i in range(n - 1):
    res.append(route[res[i]][visit])
    visit |= (1 << res[-1])
for i in range(n):
    res[i] += 1
res.append(1)
print(*res)