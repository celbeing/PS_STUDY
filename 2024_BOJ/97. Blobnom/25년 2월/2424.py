# 2424: 부산의 해적
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    n, m = map(int, input().split())
    t_map = [[0] * m for _ in range(n)]
    s_bfs = deque()
    p_bfs = deque()
    s_check = [[0] * m for _ in range(n)]
    p_check = [[0] * m for _ in range(n)]

    def pirate(i, j):
        for k in range(4):
            x, y = i, j
            while 0 <= x < n and 0 <= y < m and t_map[x][y] != 1:
                t_map[x][y] = -1
                x += d[k][0]
                y += d[k][1]
    px, py = 0, 0
    for i in range(n):
        line = list(input().strip())
        for j in range(m):
            if line[j] == 'I':
                t_map[i][j] = 1
            elif line[j] == 'Y':
                s_bfs.append((i, j))
                s_check[i][j] = 1
            elif line[j] == 'V':
                p_bfs.append((i, j))
                p_check[i][j] = 1
                px, py = i, j
            elif line[j] == 'T':
                t_map[i][j] = 2
    pirate(px, py)

    while s_bfs:
        t = len(p_bfs)
        for _ in range(t):
            x, y = p_bfs.popleft()
            for k in range(4):
                nx, ny = x + d[k][0], y + d[k][1]
                if 0 <= nx < n and 0 <= ny < m and p_check[nx][ny] == 0 and t_map[nx][ny] != 1:
                    p_bfs.append((nx, ny))
                    p_check[nx][ny] = 1
                    pirate(nx, ny)
        t = len(s_bfs)
        for _ in range(t):
            x, y = s_bfs.popleft()
            for k in range(4):
                nx, ny = x + d[k][0], y + d[k][1]
                if 0 <= nx < n and 0 <= ny < m:
                    if s_check[nx][ny] == 0 and t_map[nx][ny] == 0:
                        s_bfs.append((nx, ny))
                        s_check[nx][ny] = 1
                    elif t_map[nx][ny] == 2:
                        print('YES')
                        return

    print('NO')
    return
solution()