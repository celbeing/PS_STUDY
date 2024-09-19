#22115: 창영이와 커피
import sys
input = sys.stdin.readline
def solution():
    N, K = map(int, input().split())
    cof = [0] + list(map(int, input().split()))
    dp = [[-1] * (K + 1) for _ in range(N + 1)]
    dp[0][0] = 0
    for i in range(1, N + 1):
        for j in range(0, K + 1):
            if dp[i - 1][j] >= 0:
            if j >= cof[i - 1]: k += dp[i - 1][j - cof[i - 1]][0]
        if dp[i][-1]: return i
    return -1
print(solution())