# 20918: 좋은 배열 세기
import sys
input = sys.stdin.readline
mod = int(1e9 + 7)
dp = [[0] * (1001) for _ in range(1001)]
for i in range(1, 1001):
    dp[i][0] = 1
    r = (i + 2) * (i - 1) // 2
    for j in range(1, min(r + 1, 1001)):
        dp[i][j] = dp[i - 1][j] +dp[i][j - 1] - (dp[i - 1][j - i - 1] if i < j else 0)
        dp[i][j] %= mod
for i in range(1, 1001):
    r = (i + 2) * (i - 1) // 2
    for j in range(1, min(r + 1, 1001)):
        dp[i][j] += dp[i][j - 1]
        dp[i][j] %= mod

for _ in range(int(input())):
    n, a, b = map(int, input().split())
    res = (dp[n][b] - dp[n][a - 1]) % mod if a else dp[n][b]
    print(res)