# 1613: 역사
import sys
input = sys.stdin.readline
def solution():
    n, k = map(int, input().split())
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    for _ in range(k):
        u, v = map(int, input().split())
        graph[u][v] = 1
        graph[v][u] = -1
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            if i == k: continue
            for j in range(1, n + 1):
                if j == k: continue
                if graph[i][j] == 0:
                    if graph[i][k] == graph[k][j] == 1:
                        graph[i][j] = 1
                        graph[j][i] = -1
                    elif graph[i][k] == graph[k][j] == -1:
                        graph[i][j] = -1
                        graph[j][i] = 1
    for _ in range(int(input())):
        u, v = map(int, input().split())
        print(-graph[u][v])
solution()