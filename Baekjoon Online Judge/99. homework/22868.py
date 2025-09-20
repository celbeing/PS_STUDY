# 22868: 산책 (small)
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, m = map(int, input().split())
link = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    link[a].append(b)
    link[b].append(a)
for i in range(1, n + 1):
    link[i].sort()
s, e = map(int, input().split())
