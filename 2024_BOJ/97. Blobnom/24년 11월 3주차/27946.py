# 27945: 슬슬 가지를 먹지 않으면 죽는다
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    date = [dict() for _ in range(n + 1)]
    link = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, t = map(int, input().split())
        date[u][v] = t
        date[v][u] = t
        link[u].append(v)
        link[v].append(u)

    head = [i for i in range(n + 1)]
    
    def union(a, b):
        A = find(a)
        B = find(b)
        if A == B:
            return False
        elif A < B:
            head[b] = A
        else:
            head[a] = B
        return True

    def find(k):
        while head[k] != k:
            k = head[k]
        return k

    near = []
    heappush(near, (0, 1))
    for i in range(1, n):
        k, now = heappop(near)
        for 


solution()