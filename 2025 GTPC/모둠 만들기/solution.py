# X1 모둠 만들기1
# SOLUITON BY 김명서

import sys
input = sys.stdin.readline
INF = int(1e9)

N, A, B = map(int, input().split())
S = sorted([-INF] + list(map(int, input().split())))
dp = [INF] * (N + 1); dp[0] = 0

for i in range(A, N + 1):
    for j in range(i - A + 1, max(i - B, 0), -1):
        diff = S[i] - S[j]
        dp[i] = min(dp[i], dp[j - 1] + diff)

print(dp[N] if dp[N] < INF else -1)