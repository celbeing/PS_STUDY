# 33960: 사과 게임
import sys
input = sys. stdin.readline

n = int(input())
a = list(map(int, input().split()))
s = [0] * n
s[0] = a[0]
for i in range(1, n):
    s[i] = s[i - 1] + a[i]

dp = [[-1] * n for _ in range(n)]
for i in range(n): dp[i][i] = 0

def pf(i, j):
    return s[j] - s[i] + a[i]

def dfs(i, j):
    if dp[i][j] == -1:
        if pf(i, j) == 10:
            dp[i][j] = 1
            return dp[i][j]

        dp[i][j] = 0
        prefix_sum = pf(i, j)
        for k in range(i, j):
            left = dfs(i, k)
            right = dfs(k + 1, j)
            if prefix_sum == (left + right) * 10:
                dp[i][j] = max(dp[i][j], dp[i][k] + dp[k + 1][j])
            elif prefix_sum - (left + right) * 10 == 10:
                dp[i][j] = max(dp[i][j], dp[i][k] + dp[k + 1][j] + 1)
            else:
                dp[i][j] = max(dp[i][j], dp[i][k] + dp[k + 1][j])
    return dp[i][j]

dfs(0, n - 1)
print(dp[0][-1])