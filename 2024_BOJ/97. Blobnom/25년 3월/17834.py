# 17834: 사자와 토끼
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    check = [0] * (n + 1)
    count = [0] * 3
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    is_bipartite = True
    bfs = deque([1])
    check[1] = 1
    count[1] = 1
    while bfs:
        now = bfs.popleft()
        for next in graph[now]:
            if check[now] == check[next]:
                is_bipartite = False
                bfs.clear()
                break
            elif check[next] == 0:
                check[next] = check[now] * -1
                count[check[next]] += 1
                bfs.append(next)
    if is_bipartite:
        print(count[1] * count[2] * 2)
    else:
        print(0)
solution()