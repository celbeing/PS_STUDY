# 3050: 집들이
import sys
input = sys.stdin.readline
def solution():
    r, c = map(int, input().split())
    layout = [list(input().strip()) for _ in range(r)]
    width = [[0] * c for _ in range(r)]
    res = 0
    for i in range(r):
        if layout[i][-1] == '.':
            width[i][-1] = 1
        for j in range(c - 2, -1, -1):
            if layout[i][j] == 'X': continue
            else: width[i][j] = width[i][j + 1] + 1
    for i in range(r):
        for j in range(c):
            if width[i][j] == 0: continue
            w = width[i][j]
            p = w * 2 + 2
            if res < p:
                res = p
            for k in range(r - i):
                if layout[i + k][j] == 'X': break
                if w > width[i + k][j]:
                    w = width[i + k][j]
                p = (w + k + 1) * 2
                if res < p:
                    res = p
    print(res - 1)
solution()