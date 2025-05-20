# 20128: Parity Constraint Shortest Path
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    inf = int(1e16)
    graph = [dict() for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        graph[u][v] = w
        graph[v][u] = w
    even = [inf] * (n + 1)
    odd = [inf] * (n + 1)
    even[1] = 0
    bfs = deque([(1, 0)])
    while bfs:
        now, dist = bfs.popleft()
        for next in graph[now]:
            new = dist + graph[now][next]
            if new & 1:
                if odd[next] > new:
                    odd[next] = new
                    bfs.append((next, new))
            else:
                if even[next] > new:
                    even[next] = new
                    bfs.append((next, new))
    for i in range(1, n + 1):
        if even[i] == inf: even[i] = -1
        if odd[i] == inf: odd[i] = -1
        print(odd[i], even[i])
solution()