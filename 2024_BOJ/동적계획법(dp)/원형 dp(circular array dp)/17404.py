#17404: RGB거리 2
import sys
input = sys.stdin.readline
N = int(input())
cost = [list(map(int,input().split())) for _ in range(N)]
dp = [[0]*3 for _ in range(3)]

for i in range(3):
    for j in range(3):
        dp[i][j] = cost[0][i]+cost[1][j]
    dp[i][i] = 1000000

for i in range(2,N):
    for j in range(3):
        r = min(dp[j][1],dp[j][2])+cost[i][0]
        g = min(dp[j][0],dp[j][2])+cost[i][1]
        b = min(dp[j][0],dp[j][1])+cost[i][2]
        dp[j][0] = r
        dp[j][1] = g
        dp[j][2] = b

result = 1000000
for i in range(3):
    for j in range(3):
        if i == j: continue
        if dp[i][j] < result:
            result = dp[i][j]

print(result)