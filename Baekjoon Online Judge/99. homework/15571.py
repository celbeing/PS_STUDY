# 15571: 블록 3
import sys
input = sys.stdin.readline
mod = 1999

n, m = map(int, input().split())
dp = [0] * (m + 1)
pre = [0] * (m + 1)
dp[0] = pre[0] = 1

for i in range(1, m + 1):
    dp[i] +=