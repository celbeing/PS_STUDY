#22115: 창영이와 커피
import sys
input = sys.stdin.readline
def solution():
    N, K = map(int, input().split())
    cof = list(map(int, input().split()))
    dp = [int(1e9)] * (K + 1)
    dp[0] = 0
    for c in cof:
        for k in range(K - c, -1, -1):
            dp[k + c] = min(dp[k + c], dp[k] + 1)
    return dp[-1] if dp[-1] < 1e9 else -1
print(solution())