# 2887: 행성 터널
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
def solution():
    n = int(input())
    x, y, z = [], [], []
    for i in range(n):
        a, b, c = map(int, input().split())
        x.append((a, i))
        y.append((b, i))
        z.append((c, i))
    x.sort()
    y.sort()
    z.sort()

    hq = []
    for i in range(1, n):
        heappush(hq, (x[i][0] - x[i - 1][0], x[i][1], x[i - 1][1]))
        heappush(hq, (y[i][0] - y[i - 1][0], y[i][1], y[i - 1][1]))
        heappush(hq, (z[i][0] - z[i - 1][0], z[i][1], z[i - 1][1]))

    head = [i for i in range(n)]

    def find(k):
        while k != head[k]:
            k = head[k]
        return k

    def union(a, b):
        A = find(a)
        B = find(b)
        if A < B:
            head[A] = b
        else:
            head[B] = a
        return

    cost = 0
    count = 1
    while count < n:
        d, u, v = heappop(hq)
        if find(u) == find(v): continue
        else:
            union(u, v)
            count += 1
            cost += d
    print(cost)
solution()