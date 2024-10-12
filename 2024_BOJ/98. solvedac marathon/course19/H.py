#15910: 바나나나빠나나
import sys
input = sys.stdin.readline
def solution():
    S = ['.'] + list(input().rstrip())
    dp = [[int(1e9)] * 7 for _ in range(len(S))]
    dp[0][0] = 0
    for i in range(1, len(S)):
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][1]) + (0 if S[i] == 'B' else 1)
        dp[i][1] = min(dp[i][1], dp[i - 1][6] + (0 if S[i] == 'B' else 1))
        dp[i][2] = dp[i - 1][1] + (0 if S[i] == 'A' else 1)
        dp[i][3] = dp[i - 1][2] + (0 if S[i] == 'N' else 1)
        dp[i][4] = dp[i - 1][3] + (0 if S[i] == 'A' else 1)
        dp[i][5] = min(dp[i - 1][4], dp[i - 1][6]) + (0 if S[i] == 'N' else 1)
        dp[i][6] = dp[i - 1][5] + (0 if S[i] == 'A' else 1)
    print(dp[len(S) - 1][6])
solution()