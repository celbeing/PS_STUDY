# 11583: 인경호의 징검다리
import sys
input = sys.stdin.readline
def solution():
    inf = int(1e6)
    for _ in range(int(input())):
        n, k = map(int, input().split())
        s = list(map(int, input().split()))
        f = [[0, 0] for _ in range(n)]
        for i in range(n):
            a = s[i]
            while a % 2 == 0:
                a //= 2
                f[i][0] += 1
            while a % 5 == 0:
                a //= 5
                f[i][1] += 1
        dp = [[inf, inf, inf, inf] for _ in range(n)]
        dp[0] = [f[0][0], f[0][1]]
        for i in range(1, n):
            for j in range(max(0, i - k), i):
                if dp[i][0] > dp[j][0] + f[i][0]:
                    dp[i][0] = dp[j][0] + f[i][0]
                if dp[i][1] > dp[j][1] + f[i][1]:
                    dp[i][1] = dp[j][1] + f[i][1]
        print(min(dp[-1]))
solution()