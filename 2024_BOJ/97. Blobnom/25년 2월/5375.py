# 5375: 공책 구매
import sys
input = sys.stdin.readline
def solution():
    inf = int(2e8)
    for _ in range(int(input())):
        n, m = map(int, input().split())
        dp = [[inf] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 0
        notes = [tuple(map(int, input().split())) for _ in range(m)]
        notes.sort(key = lambda x: x[1])
        k = 1
        for s, p, o in notes:
            for i in range(n + 1):
                if dp[k - 1][i] == inf: continue
                dp[k][i] = min(dp[k - 1][i], dp[k][i])
                max_count = min(s, n - i)
                dp[k][i + max_count] = min(dp[k][i + max_count], dp[k - 1][i] + o + p * max_count)
            k += 1
        print(dp[m][n])
solution()