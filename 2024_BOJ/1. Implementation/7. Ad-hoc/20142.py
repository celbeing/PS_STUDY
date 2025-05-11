# 20142: Vista 5
import sys
input = sys.stdin.readline
def solution():
    f = open(r"C:\Users\kimsd\Downloads\5.in", "r")
    n = int(f.readline())
    dots = []
    for i in range(1, n + 1):
        x, y = map(int, f.readline().split())
        dots.append((x, y, i))
    dots.sort()
    res = []
    res.append(dots[0][2])
    for i in range(0, 100, 2):
        for j in range(1, 100):
            res.append(dots[i * 100 + j][2])
        for j in range(99, 0, -1):
            res.append(dots[(i + 1) * 100 + j][2])
    for i in range(9900, -1, -100):
        res.append(dots[i][2])
    print(*res)
solution()