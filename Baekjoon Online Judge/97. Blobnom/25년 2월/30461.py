# 30461: 낚시
import sys
input = sys.stdin.readline
def solution():
    n, m, q = map(int, input().split())
    fish = [list(map(int, input().split())) for _ in range(n)]
    for j in range(m):
        for i in range(1, n):
            fish[i][j] += fish[i - 1][j]
    for i in range(n):
        a, b = i + 1, 1
        while a < n and b < m:
            fish[a][b] += fish[a - 1][b - 1]
            a += 1
            b += 1
    for j in range(1, m):
        a, b = 1, j + 1
        while a < n and b < m:
            fish[a][b] += fish[a - 1][b - 1]
            a += 1
            b += 1
    for _ in range(q):
        w, p = map(int, input().split())
        print(fish[w - 1][p - 1])
solution()