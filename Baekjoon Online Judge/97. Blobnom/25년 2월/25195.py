# 25195: Yes or yes
import sys
input = sys.stdin.readline
from collections import deque
def solution():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    check = [0] * (n + 1)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
    s = int(input())
    fan = list(map(int, input().split()))
    for f in fan:
        check[f] = -1

    fin = False
    bfs = deque([1])
    while bfs:
        now = bfs.popleft()
        if check[now] == -1: continue

        if graph[now]:
            for next in graph[now]:
                if check[next] == 0:
                    check[next] = 1
                    bfs.append(next)
        else:
            fin = True
            break

    print('yes' if fin else 'Yes')
solution()