# 32402: TPS
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    px, py, cx, cy = 0, 0, 0, -1
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    rx = [-1, 1, 1, -1]
    ry = [1, 1, -1, -1]
    d = 0
    for _ in range(n):
        q = input().strip()
        if q == 'W':
            px += dx[d]
            py += dy[d]
            cx += dx[d]
            cy += dy[d]
        elif q == 'S':
            px -= dx[d]
            py -= dy[d]
            cx -= dx[d]
            cy -= dy[d]
        elif q == 'A':
            px += dx[d - 1]
            py += dy[d - 1]
            cx += dx[d - 1]
            cy += dy[d - 1]
        elif q == 'D':
            px -= dx[d - 1]
            py -= dy[d - 1]
            cx -= dx[d - 1]
            cy -= dy[d - 1]
        elif q == 'MR':
            cx += rx[d]
            cy += ry[d]
            d += 1
            d %= 4
        else:
            d -= 1
            d %= 4
            cx -= rx[d]
            cy -= ry[d]
        print(px, py, cx, cy)
solution()