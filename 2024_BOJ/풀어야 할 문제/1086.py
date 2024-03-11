#1086: 박성원
import sys
from math import gcd, factorial
input = sys.stdin.readline

def dfs(L, visit, remain):
    if visit == (1<<n)-1:
        if remain == 0:
            return 1
        else:
            return 0

    if dp[visit][remain] >= 0:
        return dp[visit][remain]


N = int(input())
n = [int(input()) for _ in range(N)]
K = int(input())
dp = [[-1] * K for _ in range(1 << N)]
for i in range(N):
    dp[i][0] %= K
    for j in range(1,N):
        dp[i][j] = (dp[i][j - 1] * 10) % K