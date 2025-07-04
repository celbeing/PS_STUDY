# 2933: 미네랄
import sys
from collections import deque
input = sys.stdin.readline

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
r, c = map(int, input().split())
cave = [list(input().strip()) for _ in range(r)]

def throw(h, dir):
    x = r - h
    y = 0 if dir == 1 else c - 1
    while 0 <= y < c:
        if cave[x][y] == 'x':
            cave[x][y] = '.'
            break
        y += dir
    fall()

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
                        if 0 <= dx < r and 0 <= dy < c and check[dx][dy] == 0 and cave[dx][dy] == 'x':
                            bfs.append((dx, dy))
                            check[dx][dy] = 1
                            cluster.append((dx, dy))
                            if dx == r - 1: air = False
                if air:
                    dist = [r] * c
                    cluster.sort(reverse = True)
                    c_check = set()
                    
                    for x, y in cluster:
                        if y in c_check: continue
                        c_check.add(y)
                        nx = x + 1
                        dist[y] = 0
                        while nx < r and cave[nx][y] == '.':
                            dist[y] += 1
                            nx += 1
                    drop = min(dist)
                    for x, y in cluster:
                        cave[x][y] = '.'
                        cave[x + drop][y] = 'x'
                    return

n = int(input())
a = list(map(int, input().split()))
dir = 1
for i in range(n):
    throw(a[i], dir)
    dir *= -1
for i in range(r):
    print(''.join(cave[i]))