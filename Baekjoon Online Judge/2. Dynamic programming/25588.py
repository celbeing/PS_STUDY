# 25588: 푸앙이와 계단 수열
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = [0] + list(map(int, input().split()))
stair = [i for i in range(n + 1)]
dp = [100000] * (n + 1)
dp[0] = 0
dp[1] = 1
dp[2] = 1
dp[3] = 1
if abs(a[1] - a[2]) == 1: stair[2] = 0
if abs(a[2] - a[3]) == 1: stair[3] = stair[2]
for i in range(4, n + 1):
    if abs(a[i - 1] - a[i]) == 1: stair[i] = stair[i - 1]
    dp[i] = min(dp[i - 1], min(dp[i - 2], dp[i - 3])) + 1
    if i - stair[i] + 1 >= k:
        dp[i] = min(dp[i], dp[i - k] + 1)
print(dp[-1])