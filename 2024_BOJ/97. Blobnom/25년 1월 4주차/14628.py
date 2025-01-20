# 14628: 입 챌린저
import sys
input = sys.stdin.readline
def solution():
    n, m, k = map(int, input().split())
    inf = int(1e9)
    dp = [[inf] * (m + 1) for _ in range(n + 1)]
    check = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i - 1][0] = 0
        check[i - 1][0] = 1
        x, y = map(int, input().split())
        for j in range(m + 1):
            if check[i - 1][j]:
                if dp[i][j] > dp[i - 1][j]:
                    dp[i][j] = dp[i - 1][j]
                    check[i][j] = 1
                a, b, c = x, j + y, x
                while b <= m:
                    if dp[i][b] > dp[i - 1][j] + a:
                        dp[i][b] = dp[i - 1][j] + a
                    check[i][b] = 1
                    c += k
                    a += c
                    b += y
    print(dp[n][m])
solution()