# 22975: 도시 계획
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    h = list(map(int, input().split()))
    inc = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            inc.append(((h[j] - h[i]) / (j - i), i, j))
    inc.sort(key = lambda x: (x[0], x[2]))
    dp = [1] * n
    for i, a, b in inc:
        dp[b] = max(dp[b], dp[a] + 1)
    print(n - max(dp))
solution()