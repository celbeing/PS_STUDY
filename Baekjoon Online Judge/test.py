import sys
input = sys.stdin.readline
mod = int(1e9 + 9)

n = int(input())
a = list(map(int, input().split()))
dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 1
for i in range(1, n + 1):
    for j in range(i):
        dp[i][j]