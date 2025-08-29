# 3075: Astromeeting
import sys
input = sys.stdin.readline
INF = int(1e12)

def solution():
    n, p, q = map(int, input().split())
    dist = [[INF] * (p + 1) for _ in range(p + 1)]
    for i in range(1, p + 1): dist[i][i] = 0
    now = []
    for _ in range(n): now.append(int(input()))
    for _ in range(q):
        i, j, d = map(int, input().split())
        dist[i][j] = min(dist[i][j], d)
        dist[j][i] = min(dist[i][j], d)

    for k in range(1, p + 1):
        for i in range(1, p + 1):
            for j in range(1, p + 1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    num = 0
    res = INF
    for i in range(1, p + 1):
        sum = 0
        for N in now:
            sum += dist[i][N] ** 2
            if sum > res:
                break
        if res > sum:
            res = sum
            num = i

    print(num, res)

for _ in range(int(input())): solution()