# 2276: 물 채우기
import sys
from heapq import heappush, heappop
from collections import deque
input = sys.stdin.readline
def solution():
    d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    m, n = map(int, input().split())
    bottle = [list(map(int, input().split())) for _ in range(n)]
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            low = int(1e9)
            bfs = deque([(i, j)])
            while bfs:
                x, y = bfs.popleft()
                for k in range(4):
                    dx, dy = x + d[k][0], y + d[k][1]
                    if 0 <= dx < n and 0 <= dy < m:
                        if low > 
    return
solution()