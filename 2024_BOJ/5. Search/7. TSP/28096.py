# 28096: 도시락 배달
import sys
input = sys.stdin.readline

inf = 5_000_000

def TSP(now, visit):
    if dp[now][visit] == inf:
        for i in range(1, n + 1):
            if visit & 1 << i: continue
            dp[now][visit] = min(dp[now][visit], TSP(i, visit | 1 << i) + dist[now][i])
    return dp[now][visit]

for _ in range(int(input())):
    f, w, l, n = map(int, input().split())
    loc = []
    dist = [[inf] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        loc.append(tuple(map(int, input().split())))
        for j in range(i):
            if loc[i][0] == loc[j][0]:
                d = abs(loc[i][1] - loc[j][1]) + abs(loc[i][2] - loc[j][2])
                dist[i][j] = d
                dist[j][i] = d
            else:
                d = min(loc[i][1] + loc[j][1] - 2, w * 2 - (loc[i][1] + loc[j][1])) + min(loc[i][2] + loc[j][2] - 2, l * 2 - (loc[i][2] + loc[j][2])) + abs(loc[i][0] - loc[j][0])
                dist[i][j] = d
                dist[j][i] = d
                if loc[i][0] > loc[j][0]:
                    dist[j][i] += abs(loc[i][0] - loc[j][0])
                else:
                    dist[i][j] += abs(loc[i][0] - loc[j][0])

    dp = [[inf] * (1 << (n + 1)) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][(1 << (n + 1)) - 1] = 0

    print(TSP(0, 1))