# 2638: 치즈
import sys
from collections import deque
input = sys.stdin.readline
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

n, m = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(n)]
count = 0
for i in range(n):
    for j in range(m):
        if cheese[i][j]: count += 1

def melt():
    check = [[0] * m for _ in range(n)]
    over = []
    bfs = deque([(0, 0)])
    check[0][0] = 1
    while bfs:
        x, y = bfs.popleft()
        for k in range(4):
            dx, dy = x + d[k][0], y + d[k][1]
            if 0 <= dx < n and 0 <= dy < m:
                if cheese[dx][dy]:
                    check[dx][dy] -= 1
                    if check[dx][dy] == -2:
                        over.append((dx, dy))
                elif cheese[dx][dy] == 0 and check[dx][dy] == 0:
                    bfs.append((dx, dy))
                    check[dx][dy] = 1

    for x, y in over:
        cheese[x][y] = 0

    return len(over)

day = 0
while count:
    count -= melt()
    day += 1

print(day)