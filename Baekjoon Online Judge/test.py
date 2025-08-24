import sys
input = sys.stdin.readline
INF = int(1e9)

def solution():
    n, m = map(int, input().split())
    invalid = set()
    for _ in range(m): invalid.add(int(input()))
    p, q = 0, 1
    while p <= n:
        p += q
        q += 1

    dp = [[INF] * q for _ in range(n + 1)]
    dp[1][0] = 0
    result = INF
    for i in range(1, n + 1):
        if i in invalid: continue
        for j in range(q):
            if dp[i][j] == INF: continue
            for k in range(-1, 2, 1):
                next = i + j + k
                if i < next <= n and not(next in invalid):
                    dp[next][j + k] = min(dp[next][j + k], dp[i][j] + 1)
                    if next == n:
                        result = min(result, dp[next][j + k])
    if result == INF:
        print(-1)
    else:
        print(result)

solution()