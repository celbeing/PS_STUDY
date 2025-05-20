# 32251: 나무 물 주기
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n, q = map(int, input().split())
    link = [[] for _ in range(n + 1)]
    tree = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        link[u].append(v)
        link[v].append(u)
    check = [0] * (n + 1)
    check[1] = 1
    bfs = deque([1])
    while bfs:
        now = bfs.popleft()
        for next in link[now]:
            if check[next]: continue
            tree[now].append(next)
            check[next] = 1
            bfs.append(next)
    fruit = [0] + list(map(int, input().split()))
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            water = deque([(query[1], query[2])])
            while water:
                u, x = water.popleft()
                k = min(fruit[u], x)
                fruit[u] += k
                x -= k
                if len(tree[u]):
                    x //= len(tree[u])
                    if x:
                        for next in tree[u]:
                            water.append((next, x))
        else:
            print(fruit[query[1]])
solution()