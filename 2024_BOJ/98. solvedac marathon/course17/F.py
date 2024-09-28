#23831: 나 퇴사임?
import sys
input = sys.stdin.readline
def solution():
    N = int(input())
    A, B = map(int, input().split())
    sat = [tuple(map(int, input().split())) for _ in range(N)]
    sat.reverse()
    dp = [[[[0] * 2 for _ in range(101)] for _ in range(101)] for _ in range(101)]
    p, q, r, s = sat.pop()
    dp[1][0][1][0] = max(p, q)
    dp[1][1][0][0] = s
    dp[1][0][0][1] = r
    for n in range(2, N + 1):
        p, q, r, s = sat.pop()
        t = max(p, q)
        for b in range(n + 1):
            for a in range(n - b + 1):
                study, rest = 0, 0
                if a: rest = max(dp[n - 1][a - 1][b]) + s
                if b: study = max(dp[n - 1][a][b - 1]) + t
                dp[n][a][b][0] = max(study, rest)
                dp[n][a][b][1] = dp[n - 1][a][b][0] + r
    high = 0
    for a in range(A + 1):
        for b in range(B, N + 1):
            high = max(high, max(dp[N][a][b]))
    print(high)
solution()