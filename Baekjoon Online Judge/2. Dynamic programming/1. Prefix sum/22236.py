# 22236: 가희와 비행기
import sys
input = sys.stdin.readline

def solution():
    d, m = map(int, input().split())
    d >>= 1
    dp = [1] * d
    for i in range(2, d):
        for j in range(i, d):
            dp[j] += dp[j - 1]
            dp[j] %= m
    print(dp[-1])
solution()