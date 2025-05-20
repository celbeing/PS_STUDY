# 14938: 서강그라운드
import sys
input = sys.stdin.readline
def solution():
    inf = int(1e6)
    n, m, r = map(int, input().split())
    t = [0] + list(map(int, input().split()))
    road = [[inf] * (n + 1) for _ in range(n + 1)]
    for _ in range(r):
        u, v, w = map(int, input().split())
        if road[u][v] > w:
            road[u][v] = w
            road[v][u] = w

    for k in range(1, n + 1):
        road[k][k] = 0
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                road[i][j] = min(road[i][j], road[i][k] + road[k][j])

    item = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if road[i][j] <= m:
                item[i] += t[j]
    print(max(item))
solution()