# 11997: Load Balancing (Silver)
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    cow = [[0] * 1001 for _ in range(1001)]
    cor = []
    cor_x = set()
    cor_y = set()
    for _ in range(n):
        x, y = map(int, input().split())
        cor_x.add(x)
        cor_y.add(y)
        cor.append((x, y))
    cor_x = sorted(list(cor_x))
    cor_y = sorted(list(cor_y))
    corzip_x = dict()
    corzip_y = dict()
    k = 1
    for X in cor_x:
        corzip_x[X] = k
        k += 1
    k = 1
    for Y in cor_y:
        corzip_y[Y] = k
        k += 1
    for x, y in cor:
        cow[corzip_x[x]][corzip_y[y]] += 1
    for i in range(1001):
        for j in range(1, 1001):
            cow[i][j] += cow[i][j - 1]
    for i in range(1001):
        for j in range(1, 1001):
            cow[j][i] += cow[j - 1][i]
    result = 1000
    for i in range(1001):
        for j in range(1001):
            h = cow[-1][j] - cow[i][j]
            v = cow[i][-1] - cow[i][j]
            o = n - h - v - cow[i][j]
            result = min(result, max(h, v, o, cow[i][j]))
    print(result)
solution()