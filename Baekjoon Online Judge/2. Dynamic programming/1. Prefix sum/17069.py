# 17069: 파이프 옮기기 2
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]
    for i in range(1, n):
        if grid[0][i]: break
        dp[0][i][0] = 1
    for i in range(1, n):
        for j in range(1, n):
            if grid[i][j]: continue
            dp[i][j][0] += dp[i][j - 1][0] + dp[i][j - 1][1]
            dp[i][j][2] += dp[i - 1][j][1] + dp[i - 1][j][2]
            if grid[i - 1][j] == grid[i][j - 1] == 0:
                dp[i][j][1] += sum(dp[i - 1][j - 1])
    print(sum(dp[-1][-1]))
solution()