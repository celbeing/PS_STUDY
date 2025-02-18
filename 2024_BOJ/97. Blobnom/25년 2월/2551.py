# 2551: 두 대표 자연수
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    a = sorted(list(map(int, input().split())))
    x = a[(n - 1) >> 1]
    y = round(sum(a) / n)
    if y ** 2 - sum(a) * y * 2 / n >= (y - 1) ** 2 - sum(a) * (y - 1) * 2 / n:
        y -= 1
    print(x, y)
solution()