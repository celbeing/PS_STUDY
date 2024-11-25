# 25603: 짱해커 이동식
import sys
input = sys.stdin.readline
def solution():
    N, K = map(int, input().split())
    req = list(map(int, input().split()))
    dp = [int(1e15)] * N
    for i in range(K):
        dp[i] = req[i]
    for i in range(K, N):
        for j in range(i - K, i):
            dp[i] = min(dp[i], dp[j])
        dp[i] += req[i]
    res = dp[-1]
    for i in range(N - K, N):
        res = min(res, dp[i])
    print(res)
solution()