import sys
input = sys.stdin.readline
T = int(input())
k = int(input())
coins = [tuple(map(int,input().split())) for _ in range(k)]
dp = [[0]*(T+1) for _ in range(k+1)]
dp[0][0] = 1
for i in range(k):
    p,n = coins[i]
    for j in range(T+1):
        if dp[i][j]:
            pn = 0
            for s in range(j,T+1,p):
                if pn > n: break
                dp[i+1][s] += dp[i][j]
                pn += 1
print(dp[-1][-1])