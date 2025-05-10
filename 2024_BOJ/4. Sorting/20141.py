# 20141: Vista 4
import sys
input = sys.stdin.readline
f = open(r"C:\Users\kimsd\Downloads\4.in", "r")
def solution():
    n = int(f.readline().strip())
    dots = []
    for i in range(1, n + 1):
        x, y = map(int, f.readline().strip().split())
        dots.append((x, y, i))
        dots.sort()
    for x, y, i in dots:
        print(i)
    print(dots[0][2])
solution()