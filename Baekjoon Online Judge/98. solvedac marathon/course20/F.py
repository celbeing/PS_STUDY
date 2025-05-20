#9029: 정육면체
import sys
input = sys.stdin.readline

def solution():
    dp = [[[0] * 201 for _ in range(201)] for _ in range(201)]
    dp[1][1][1] = 1
    for i in range(1, 201):
        for j in range(1, 201):
            for k in range(1, 201):
                if dp[i][j][k]: continue
                elif i == 1: dp[i][j][k] = j * k
                elif j == 1: dp[i][j][k] = i * k
                elif k == 1: dp[i][j][k] = i * j
                elif i % k == j % k == 0:
                    dp[i][j][k] = (i // k) * (j // k)
                elif i % j == k % j == 0:
                    dp[i][j][k] = (i // j) * (k // j)
                elif j % i == k % i == 0:
                    dp[i][j][k] = (j // i) * (k // i)
                else:
                    dp[i][j][k] = 8000000
                    for h in range(1, i):
                        dp[i][j][k] = min(dp[i][j][k], dp[h][j][k] + dp[i-h][j][k])
                    for w in range(1, j):
                        dp[i][j][k] = min(dp[i][j][k], dp[i][w][k] + dp[i][j-w][k])
                    for l in range(1, k):
                        dp[i][j][k] = min(dp[i][j][k], dp[i][j][l] + dp[i][j][k-l])
                dp[i][k][j] = dp[j][i][k] = dp[j][k][i] = dp[k][i][j] = dp[k][j][i] = dp[i][j][k]
    for _ in range(int(input())):
        h, w, l = map(int, input().split())
        print(dp[h][w][l])
solution()