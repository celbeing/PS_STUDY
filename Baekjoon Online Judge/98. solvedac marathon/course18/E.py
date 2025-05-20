#24956: 나는 정말 휘파람을 못 불어
import sys
input = sys.stdin.readline
def solution():
    div = int(1e9 + 7)
    N = int(input())
    S = '_' + input().rstrip()
    dp = [[0] * 5 for _ in range(N + 1)]
    for n in range(1, N + 1):
        if S[n] == 'W':
            dp[n][1] += 1
        elif S[n] == 'H':
            dp[n][2] += dp[n - 1][1]
        elif S[n] == 'E':
            dp[n][3] += dp[n - 1][2]
            dp[n][4] += dp[n - 1][3] + dp[n - 1][4]
        for i in range(1, 5):
            dp[n][i] += dp[n - 1][i]
            dp[n][i] %= div
    print(dp[N][4])
solution()