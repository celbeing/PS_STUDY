# 13237: Binary tree
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n = int(input())
    tree = [[] for _ in range(n + 1)]
    height = [0] * (n + 1)
    bfs = deque()
    for i in range(1, n + 1):
        par = int(input())
        if par == -1:
            bfs.append(i)
        else: tree[par].append(i)
    while bfs:
        now = bfs.popleft()
        for next in tree[now]:
            height[next] = height[now] + 1
            bfs.append(next)
    for i in range(1, n + 1):
        print(height[i])
solution()