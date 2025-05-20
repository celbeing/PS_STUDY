# 25489: 반짝반짝 3
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n = int(input())
    p = [0] + list(map(float, input().split()))
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    tree = [[] for _ in range(n + 1)]
    link_p = [[0, 0] for _ in range(n + 1)]
    check = [0] * (n + 1)
    tree[1].append(0)
    check[1] = 1
    bfs = deque([1])
    while bfs:
        now = bfs.popleft()
        for next in graph[now]:
            if check[next]: continue
            bfs.append(next)
            check[next] = 1
            tree[now].append(next)
            tree[next].append(now)
            link_p[now][0] += p[next]
            link_p[now][1] += 1 - p[next]
    res = sum(p)
    for i in range(1, n + 1):
        res += p[i] * link_p[i][1] + (1 - p[i]) * link_p[i][0]
    print(res)

    for _ in range(int(input())):
        u, po = map(str, input().split())
        u = int(u)
        po = float(po)
        parent = tree[u][0]
        if parent:
            res += (1 - p[parent] * 2) * (po - p[u])
            link_p[parent][0] += po - p[u]
            link_p[parent][1] += p[u] - po
        res += (po - p[u]) * link_p[u][1] + (p[u] - po) * link_p[u][0]
        res += po - p[u]
        p[u] = po
        print(res)
solution()