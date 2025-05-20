# 32189: '한국디지털미디어고등학교'는 너무 길다.
import sys
input = sys.stdin.readline
def solution():
    s = list(input().strip())
    n = len(s)
    def lcs(a, b):
        dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
        for i in range(len(a) + 1):
            for j in range(len(b) + 1):
                if i == 0 or j == 0: dp[i][j] = 0
                elif a[i - 1] == b[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return min(len(a), len(b)) - dp[-1][-1]
    if n & 1:
        print(max(lcs(s[:n // 2], s[n // 2:]), lcs(s[:n // 2 + 1], s[n // 2 + 1:])))
    else:
        print(lcs(s[:n // 2], s[n // 2:]))
solution()