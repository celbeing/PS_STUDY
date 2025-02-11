# 17268: 미팅의 저주
import sys
input = sys.stdin.readline
def solution():
    n = int(input()) >> 1
    n += 1
    mod = 987654321
    dp = [0] * n
    dp[0] = dp[1] = 1
    for i in range(2, n):
        for j in range(i):
            dp[i] += dp[i - j - 1] * dp[j]
            dp[i] %= mod
    print(dp[-1])
solution()