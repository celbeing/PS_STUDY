# 20054: 트리 가짓수 세기
import sys
input = sys.stdin.readline
def solution():
    n, k = map(int, input().split())
    mod = int(1e9) + 7
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    dp[0][0] = 1
    for i in range(1, k + 1):
        dp[i][0] = 1
        for j in range(1, min(n + 1, 1 << i)):
            for t in range(j):
                dp[i][j] += dp[i - 1][t] * dp[i - 1][j - t - 1]
                dp[i][j] %= mod
    print(dp[k][n])
solution()