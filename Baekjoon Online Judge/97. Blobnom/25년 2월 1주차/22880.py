# 22880: 봉화대
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    h = [0] + list(map(int, input().split()))
    mod = int(1e9) + 7
    dp = [0] * (n + 1)
    dp[0] = 1
    high = 0
    sum = 1
    for i in range(1, n + 1):
        dp[i] = dp[high]
        if h[high] < h[i]:
            dp[i] = sum
            high = i
        sum += dp[i]
        sum %= mod
    print(dp[n])
solution()