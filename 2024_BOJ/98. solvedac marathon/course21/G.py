#12013: 248 게임
import sys
input = sys.stdin.readline
def solution():
    N = int(input())
    dp = [[0] * N for _ in range(N)]
    for i in range(N):
        dp[i][i] = int(input())
    res = 0
    for t in range(1, N):
        for i in range(N - t):
            for k in range(i, i + t):
                if dp[i][k] == dp[k + 1][i + t] > 0:
                    dp[i][i + t] = max(dp[i][i + t], dp[i][k] + 1)
    for i in range(N):
        for j in range(N):
            res = max(dp[i][j], res)
    print(res)
solution()