# 1082: 방 번호
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    p = list(map(int, input().split()))
    m = int(input())
    dp = [0] * (m + 1)
    for i in range(1, m + 1):
        for j in range(n):
            if p[j] <= i:
                dp[i] = max(dp[i], dp[i - p[j]] * 10 + j)
    print(max(dp))
solution()