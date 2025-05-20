# 26009: 험난한 등굣길
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    N, M = map(int, input().split())
    K = int(input())
    D = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    board = [[0] * M for _ in range(N)]
    for _ in range(K):
        r, c, d = map(int, input().split())
        r -= 1; c -= 1
        board[r][c] = -1
        for i in range(d + 1):
            j = d - i
            dr, dc = r + i, c + j
            if dr < N and dc < M:
                board[dr][dc] = -1
            dr, dc = r - i, c + j
            if 0 <= dr < N and dc < M:
                board[dr][dc] = -1
            dr, dc = r + i, c - j
            if dr < N and 0 <= dc < M:
                board[dr][dc] = -1
            dr, dc = r - i, c - j
            if 0 <= dr < N and 0 <= dc < M:
                board[dr][dc] = -1

    bfs = deque([(0, 0)])
    while bfs:
        x, y = bfs.popleft()
        if x == N - 1 and y == M - 1: break
        for dx, dy in D:
            dx += x
            dy += y
            if 0 <= dx < N and 0 <= dy < M and board[dx][dy] == 0:
                board[dx][dy] = board[x][y] + 1
                bfs.append((dx, dy))
    print(f"YES\n{board[-1][-1]}" if board[-1][-1] > 0 else "NO")
solution()