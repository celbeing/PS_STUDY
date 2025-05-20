# 15485: a^jb^jc^k
import sys
input = sys.stdin.readline
def solution():
    s = list(input().strip())
    mod = int(1e9) + 7
    dp = [0] * 4
    dp[0] = 1
    for i in range(1, len(s) + 1):
        if s[i - 1] == 'a':
            dp[1] += dp[0] + dp[1]
            dp[1] %= mod
        elif s[i - 1] == 'b':
            dp[2] += dp[1] + dp[2]
            dp[2] %= mod
        elif s[i - 1] == 'c':
            dp[3] += dp[2] + dp[3]
            dp[3] %= mod
    print(dp[3])
solution()