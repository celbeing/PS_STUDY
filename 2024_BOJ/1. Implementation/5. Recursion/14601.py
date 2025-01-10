# 14600: 샤워실 바닥 깔기 (Large)
import sys
input = sys.stdin.readline
def solution():
    k = 1 << int(input())
    floor = [[0] * k for _ in range(k)]
    check = [[0] * k for _ in range(k)]
    idx = [1]
    def tile(x, y, w, dir):
        if w == 0: return
        if check[x][y] == 0:
            if dir != 3:
                floor[x][y] = idx[0]
            if dir != 4:
                floor[x + 1][y] = idx[0]
            if dir != 1:
                floor[x + 1][y + 1] = idx[0]
            if dir != 2:
                floor[x][y + 1] = idx[0]
            check[x][y] = 1
        idx[0] += 1
        w >>= 1
        tile(x, y, w, dir)
        if dir != 3:
            tile(x - w, y - w, w, 1)
        if dir != 4:
            tile(x + w, y - w, w, 2)
        if dir != 1:
            tile(x + w, y + w, w, 3)
        if dir != 2:
            tile(x - w, y + w, w, 4)

    a, b = map(int, input().split())
    a, b = k - b, a - 1
    floor[a][b] = -1
    k >>= 1
    x, y = k - 1, k - 1
    while k:
        dir = 0
        if y < b:
            if x < a:
                dir = 1
            else:
                dir = 2
        else:
            if x >= a:
                dir = 3
            else:
                dir = 4
        tile(x, y, k, dir)
        k >>= 1
        if dir == 1:
            x += k
            y += k
        elif dir == 2:
            x -= k
            y += k
        elif dir == 3:
            x -= k
            y -= k
        else:
            x += k
            y -= k
    for t in floor:
        print(*t)
solution()