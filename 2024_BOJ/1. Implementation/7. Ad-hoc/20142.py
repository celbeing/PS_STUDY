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
    for x, y, i in dots:
        res.append(i)
    res.append(dots[0][2])
    print(*res)
solution()