import sys
input = sys.stdin.readline
N,H = map(int,input().split())
dp = [0]*(H+1)
dp[0] = 1
A = list(map(int,input().split()))
for i in range(1,H+1):
    for a in A:
        if a > i: continue
        dp[i] += dp[i-a]
    dp[i] %= 1000000007
print(dp[-1])