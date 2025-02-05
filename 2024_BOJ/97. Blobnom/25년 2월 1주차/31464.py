# 31464: 초콜릿 괴도 코코 (Sweet)
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n = int(input())
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    chocolate = [list(input().strip()) for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if chocolate[i][j] == '#': count += 1
    result = []

    for i in range(n):
        for j in range(n):
            if chocolate[i][j] == '.': continue
            flag = True
            c = 0
            check = [[0] * n for _ in range(n)]
            bfs = deque()
            for k in range(4):
                ni, nj = i + d[k][0], j + d[k][1]
                if 0 <= ni < n and 0 <= nj < n and chocolate[ni][nj] == '#':
                    bfs.append((ni, nj))
                    check[ni][nj] = 1
                    c += 1
                    break

            while bfs:
                x, y = bfs.popleft()
                for k in range(4):
                    nx, ny = x + d[k][0], y + d[k][1]
                    if nx == i and ny == j: continue
                    if 0 <= nx < n and 0 <= ny < n and chocolate[nx][ny] == '#' and check[nx][ny] < 2:
            if flag: result.append((i, j ))

    print(len(result))
    for k in result:
        print(*k)