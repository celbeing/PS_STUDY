# 23762: 배드민턴 복식 팀 만들기
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    m = [0] + sorted(enumerate(list(map(int, input().split()))), key = lambda x: x[1])
    inf = int(1e9)
    rem = n % 4

    dp = [[inf] * (rem + 1) for _ in range(n + 1)]

    dp[0][0] = 0
    dp[4][0] = m[4][1] - m[1][1]
    for i in range(5, n + 1):
        dp[i][0] = dp[i - 4][0] + m[i][1] - m[i - 3][1]
        for j in range(1, rem + 1):
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 4][j] + m[i][1] - m[i - 3][1])
            dp[i][j] = min(dp[i][j], dp[i - 5][j - 1] + m[i][1] - m[i - 4][1])
    print(dp[-1][-1])
solution()