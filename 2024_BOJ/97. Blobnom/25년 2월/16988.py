# 16988: Baaaaaaaaaduk2 (Easy)
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    def count():
        check = [[0] * m for _ in range(n)]
        bfs = deque()
        ret = 0
        for i in range(n):
            for j in range(m):
                if board[i][j] == 2 and check[i][j] == 0:
                    bfs.append((i, j))
                    check[i][j] = 1
                    flag = True
                    count = 1
                    while bfs:
                        x, y = bfs.popleft()
                        for k in range(4):
                            nx, ny = x + d[k][0], y + d[k][1]
                            if 0 <= nx < n and 0 <= ny < m:
                                if board[nx][ny] == 0:
                                    flag = False
                                elif board[nx][ny] == 2 and check[nx][ny] == 0:
                                    check[nx][ny] = 1
                                    bfs.append((nx, ny))
                                    count += 1
                    if flag:
                        ret += count
        return ret

    res = 0
    for i in range(n * m):
        x = i // m
        y = i % m
        if board[x][y] == 0:
            board[x][y] = 1
            for j in range(i + 1, n * m):
                p = j // m
                q = j % m
                if board[p][q] == 0:
                    board[p][q] = 1
                    res = max(res, count())
                    board[p][q] = 0
            board[x][y] = 0

    print(res)
    return
solution()