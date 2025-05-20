# 15511: League of Overwatch at Moloco (Hard)
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    graph = [dict() for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a][b] = 1
        graph[b][a] = 1
    check = [0] * (n + 1)
    bfs = deque([])
    for i in range(1, n + 1):
        if check[i]: continue
        else:
            bfs.append(i)
            check[i] = 1
            while bfs:
                now = bfs.popleft()
                for next in graph[now]:
                    if check[now] == check[next]:
                        print('IMPOSSIBLE')
                        exit()
                    elif check[next] == 0:
                        check[next] = -check[now]
                        bfs.append(next)
    print('POSSIBLE')
solution()