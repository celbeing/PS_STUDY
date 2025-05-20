# 20443: 배드민턴 대회
import sys
input = sys.stdin.readline
def solution():
    mod = int(1e9 + 7)
    n = int(input())
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] * i + (-1 if i & 1 else 1)
        dp[i] %= mod
    rem = n % 4
    res = dp[n - rem]
    for i in range(n, n - rem, -1):
        res *= i
    for i in range(1, rem + 1):
        res //= i
    res %= mod
    print(res)
solution()