# 27945: 슬슬 가지를 먹지 않으면 죽는다
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    date = [dict() for _ in range(n + 1)]
    link = [[] for _ in range(n + 1)]
    start = 0
    early = int(1e9)
    for _ in range(m):
        u, v, t = map(int, input().split())
        if t < early:
            early = t
            start = u
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
            head[B] = A
        else:
            head[A] = B
        return True

    def find(k):
        while head[k] != k:
            k = head[k]
        return k

    hq = []
    gaji = [0, int(1e9)]
    edge = 1
    for next in link[start]:
        heappush(hq, (date[start][next], next, start))
    while hq and edge < n:
        k, now, before = heappop(hq)
        if union(now, before):
            gaji.append(k)
            edge += 1
            for next in link[now]:
                if find(now) == find(next): continue
                heappush(hq, (date[now][next], next, now))
    gaji.sort()
    for i in range(1, len(gaji)):
        if gaji[i] == i: continue
        else:
            print(i)
            break
solution()