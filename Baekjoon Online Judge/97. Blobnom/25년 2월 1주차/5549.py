# 5549: 행성 탐사
import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    k = int(input())
    prefix = [[[0] * 3 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        line = "$" + input().rstrip()
        for j in range(1, m + 1):
            if line[j] == 'J':
                prefix[i][j][0] += 1
            elif line[j] == 'O':
                prefix[i][j][1] += 1
            else:
                prefix[i][j][2] += 1
            for t in range(3):
                prefix[i][j][t] += prefix[i - 1][j][t]
    for j in range(1, m + 1):
        for i in range(1, n + 1):
            for t in range(3):
                prefix[i][j][t] += prefix[i][j - 1][t]
    for _ in range(k):
        a, b, c, d = map(int, input().split())
        res = [0] * 3
        for t in range(3):
            res[t] = prefix[c][d][t] - prefix[a - 1][d][t] - prefix[c][b - 1][t] + prefix[a - 1][b - 1][t]
        print(*res)
solution()