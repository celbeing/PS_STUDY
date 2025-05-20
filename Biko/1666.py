# 1666: preB1 한라봉 포장 1
import sys
input = sys.stdin.readline

def solution():
    inf = int(1e9)
    n = int(input())
    dp = [i for i in range(n + 1)]
    box = [3, 5, 10]
    for k in box:
        for j in range(k, n + 1):
            dp[j] = min(dp[j], dp[j - k] + 1)
    print(dp[-1])
solution()