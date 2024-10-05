import sys
input = sys.stdin.readline
def solution():
    N, X = map(int, input().split())
    dp = [0] * (X + 1)
    high = 0
    for _ in range(N):
        a,p,b,q = map(int, input().split())
        for i in range(p, X + 1, p):
            dp[i] = max(dp[i], a)
            high = max(high, dp[i])
        for j in range(q, X + 1, q):
            dp[j] = max(dp[j], b)
            high = max(dp[j], high)
    print(high)
solution()