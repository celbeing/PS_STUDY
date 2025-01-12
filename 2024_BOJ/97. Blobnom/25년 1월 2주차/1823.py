# 1823: 수확
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    v = [int(input()) for _ in range(n)]
    dp = [[0] * n for _ in range(n)]
    for k in range(1, n):
        r = n - k - 1
        dp[0][r] = dp[0][n - k] + v[n - k] * k
        dp[k][n - 1] = dp[k - 1][n - 1] + v[k - 1] * k
        for l in range(1, k):
            dp[l][r + l] = max(dp[l - 1][r + l] + v[l - 1] * k, dp[l][r + l + 1] + v[r + l + 1] * k)
    res = 0
    for i in range(n):
        k = dp[i][i] + v[i] * n
        if res < k: res = k
    print(res)
solution()