# 1640: 동전 뒤집기
import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    h = [0] * n
    v = [0] * m
    for i in range(n):
        line = list(input().strip())
        for j in range(m):
            if line[j] == '1':
                h[i] += 1
                v[j] += 1
    a, b = 0, 0
    for H in h:
        if H & 1: a += 1
    for V in v:
        if V & 1: b += 1
    if a & 1:
        print(min(a + m - b, b + n - a))
    else:
        print(min(a + b, n + m - a - b))
solution()