# 8895: 막대 배치
import sys
input = sys.stdin.readline
def solution():
    dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]
    dp[1][1][1] = 1
    for n in range(1, 21):
        for l in range(1, n + 1):
            for r in range(1, n - l + 2):
                dp[n][l][r] += dp[n - 1][l][r - 1]
                dp[n][l][r] += dp[n - 1][l - 1][r]
                dp[n][l][r] += dp[n - 1][l][r] * (n - 2)
    for _ in range(int(input())):
        n, l, r = map(int, input().split())
        print(dp[n][l][r])
solution()