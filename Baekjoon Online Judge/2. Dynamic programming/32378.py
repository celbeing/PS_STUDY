# 32378: 횃불이 키우기
import sys
input = sys.stdin.readline
def solution():
    n, k, s = map(int, input().split())
    if k > 36:
        print('MEGA')
        return

    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = s

    a = [0] + list(map(int, input().split()))

    for d in range(1, n + 1):
        if dp[d - 1][0] > 0: dp[d][0] = max(0, dp[d - 1][0] + a[d])
        for i in range(1, k + 1):
            if dp[d - 1][i] > 0: dp[d][i] = max(0, dp[d - 1][i] + a[d])
            if dp[d - 1][i - 1] > 0: dp[d][i] = max(dp[d][i], dp[d - 1][i - 1] << 1)

    res = max(dp[n])
    if res > 1e11: print('MEGA')
    elif res > 0: print(res)
    else: print(-1)

solution()