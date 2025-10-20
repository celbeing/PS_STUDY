import sys
from collections import deque
input = sys.stdin.readline

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n, m = map(int, input().split())
res = [[-1] * m for _ in range(n)]
bitmap = [list(input().strip()) for _ in range(n)]

bfs = deque()
for i in range(n):
    for j in range(m):
        if bitmap[i][j] == '1':
            res[i][j] = 0
            bfs.append((i, j))

while bfs:
    x, y = bfs.popleft()
    for k in range(4):
        nx, ny = x + d[k][0], y + d[k][1]
        if 0 <= nx < n and 0 <= ny < m and bitmap[nx][ny] == '0' and res[nx][ny] == -1:
            res[nx][ny] = res[x][y] + 1
            bfs.append((nx, ny))

for row in res:
    print(*row)