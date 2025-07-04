# 2933: 미네랄
import sys
from collections import deque

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
r, c = map(int, input().split())
cave = [list(input().strip()) for _ in range(r)]

def throw(h, dir):
    x = h - r
    y = 0 if dir == 1 else c - 1
    while 0 <= y < c:
        if cave[x][y] == 'x':
            cave[x][y] = '.'
            break
        y += dir

def fall():
    check = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if cave[i][j] == 'x' and check[i][j] == 0:
                bfs = deque([(i, j)])
                cluster = [(i, j)]
                check[i][j] = 1
                air = True
                while bfs:
                    x, y = bfs.popleft()
                    for k in range(4):
                        dx, dy = x + d[k][0], y + d[k][1]
                        if 0 <= dx < r and 0 <= dy < c and check[i][j] == 0:
                            bfs.append((dx, dy))
                            check[dx][dy] = 1
                            cluster.append((dx, dy))
                            if dx == r - 1: air = False
                if air:
                    cluster.sort(reverse = True)
                    c_check = set()
                    
                    for x, y in cluster:
                        if y in c_check: continue
                        c_check.add(y)
