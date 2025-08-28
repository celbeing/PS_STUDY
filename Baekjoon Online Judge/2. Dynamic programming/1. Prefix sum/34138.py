# 34138: 마을 짓기
import sys
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    res = [0] * min(n, m)
    grid = [['X'] * (m + 1)] + [['X'] + list(input().strip()) for _ in range(n)]
    sq = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if grid[i][j - 1] == '.': sq[i][j] = sq[i][j - 1] + 1
            else: sq[i][j] = 1
    for j in range(1, m + 1):
        streak = 0
        for i in range(1, n + 1):
            if grid[i - 1][j] == '.': streak += 1
            else: streak = 1
            if grid[i][j] == '.': sq[i][j] = 0
            else: sq[i][j] = min(sq[i][j], streak)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            sq[i][j] = min(sq[i][j], sq[i - 1][j - 1] + 1)
            for k in range(sq[i][j]):
                res[k] += 1
    for r in res: print(r)
solution()