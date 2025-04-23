# 14590: KUBC League (Small)
import sys
input = sys.stdin.readline
n = int(input())
link = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (1 << n) for _ in range(n)]

def tsp(now, visit):
    if dp[now][visit] == 0:
        for i in range(n):
            if link[now][i] == 0 or visit & (1 << i): continue
            dp[now][visit] = max(dp[now][visit], tsp(i, visit | 1 << i) + 1)
    return dp[now][visit]

def trace(now, visit, route):
    for i in range(n):
        if link[now][i] == 0 or visit & (1 << i): continue
        if dp[now][visit] == dp[i][visit | (1 << i)] + 1:
            trace(i, visit | (1 << i), route + [i + 1])
            break
    else:
        print(*route)

print(tsp(0, 1) + 1)
trace(0, 1, [1])