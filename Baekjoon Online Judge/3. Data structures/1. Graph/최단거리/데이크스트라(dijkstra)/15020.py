# 15020: Emptying the Baltic
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

d = [(1, 0), (1, 1), (0, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)]
n, m = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(n)]
flushed = [[0] * m for _ in range(n)]
x, y = map(int, input().split())
x -= 1; y -= 1
flushed[x][y] = sea[x][y]
res = -sea[x][y]
hq = []
heappush(hq, (sea[x][y], x, y))
while hq:
    h, x, y = heappop(hq)
    for k in range(8):
        nx, ny = x + d[k][0], y + d[k][1]
        if 0 <= nx < n and 0 <= ny < m and sea[nx][ny] < 0 and flushed[nx][ny] == 0:
            nh = max(h, sea[nx][ny])
            flushed[nx][ny] = nh
            heappush(hq, (nh, nx, ny))
            res -= nh
print(res)