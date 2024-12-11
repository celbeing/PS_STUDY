# 25428: 분필 도둑
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
def solution():
    def find(k):
        t = k
        while set_head[t] != t:
            t = set_head[t]
        while set_head[k] != k:
            set_head[k] = t
            k = set_head[k]
        return k

    def union(a, b):
        head = find(b)
        set_head[head] = a
        set_count[a] += set_count[head]
        return

    n = int(input())
    chalk = [0] + list(map(int, input().split()))
    set_count = [1] * (n + 1)
    set_head = [i for i in range(n + 1)]
    node = []
    check = [0] * (n + 1)
    for i in range(1, n + 1):
        heappush(node, (-chalk[i], i))
    result = -node[0][0]
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    while node:
        low, now = heappop(node)
        check[now] = 1
        for next in graph[now]:
            if chalk[now] > chalk[next] or check[next] == 0 or find(next) == find(now): continue
            union(now, next)
        result = max(result, set_count[now] * chalk[now])
    print(result)
solution()