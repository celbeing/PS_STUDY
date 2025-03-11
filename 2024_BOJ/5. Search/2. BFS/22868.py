# 22868: 산책(small)
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    for i in range(1, n + 1):
        graph[i].sort()
    s, e = map(int, input().split())
    bfs = deque([[s]])
    while bfs:
        now = bfs.popleft()
        for next in graph[now[-1]]:
            if next in now:
                if e in now and next == s:
                    print(len(now))
                    exit()
                else: continue
            bfs.append(now + [next])
solution()