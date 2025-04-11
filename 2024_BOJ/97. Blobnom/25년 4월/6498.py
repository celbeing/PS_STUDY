# 6498: 앨리어스 감마 코드
import sys
input = sys.stdin.readline
def solution():
    inf = int(1e9)
    while True:
        n = int(input())
        if n == 0: break
        dp = [[inf] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        c = [0] + list(map(int, input().split()))
        s = [0] * (n + 1)
        for i in range(1, n + 1):
            s[i] = s[i - 1] + c[i]
        opt = [[0] * (n + 1) for _ in range(n + 1)]
        for j in range(1, n + 1):
            opt[n][j] = n  # 경계 처리
            for i in range(n, j - 1, -1):
                l = opt[i][j - 1]
                r = opt[i + 1][j] if i + 1 <= n else n
                dp[i][j] = inf
                for k in range(l, r + 1):
                    t = dp[k][j - 1] + (s[i] - s[k]) * (i + j)
                    if dp[i][j] > t:
                        dp[i][j] = t
                        opt[i][j] = k

        res = dp[n][1]
        for j in range(2, n + 1):
            if res > dp[n][j]:
                res = dp[n][j]
        print(res)
solution()