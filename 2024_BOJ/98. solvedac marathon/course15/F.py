#31828: MR.DR 문자열
import sys
input = sys.stdin.readline
def solution():
    N = int(input())
    mod = int(1e9 + 7)
    dp = [[0] * 5 for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        dp[i][0] = dp[i - 1][0] * 26 % mod
        for j in range(1, 5):
            dp[i][j] += dp[i - 1][j] * 25
            dp[i][j] += dp[i - 1][j - 1]
            dp[i][j] %= mod
    print(dp[N][4])
solution()