# 21609: 상어 중학교
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    def gravity():
        for c in range(n):
            dist = 0
            for r in range(n - 1, -1, -1):
                if board[r][c] == -1:
                    dist = 0
                elif board[r][c] == -2:
                    dist += 1
                elif dist:
                    board[r + dist][c] = board[r][c]
                    board[r][c] = -2
        return

    def turn():
        new_board = [[-2] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                new_board[n - j - 1][i] = board[i][j]
        for i in range(n):
            for j in range(n):
                board[i][j] = new_board[i][j]
        gravity()
        return

    def find():
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        check = [[0] * n for _ in range(n)]
        bfs = deque([])
        blocks = []
        for i in range(n):
            for j in range(n):
                if check[i][j] == 0 and board[i][j] > 0:
                    t = board[i][j]
                    bfs.append((i, j))
                    count = 1
                    rainbow = 0
                    r, c = i, j
                    container = [(i, j)]
                    while bfs:
                        x, y = bfs.popleft()
                        for k in range(4):
                            nx = x + d[k][0]
                            ny = y + d[k][1]
                            if 0 <= nx < n and 0 <= ny < n and (board[nx][ny] == 0 or board[nx][ny] == t):
                                if check[nx][ny] == 0 and not (nx, ny) in container:
                                    if board[nx][ny] == 0: rainbow += 1
                                    else:
                                        if r > nx:
                                            r = nx
                                            c = ny
                                        elif r == nx and c > ny:
                                            c = ny
                                    container.append((nx, ny))
                                    bfs.append((nx, ny))
                                    count += 1
                    if len(container) > 1:
                        for x, y in container:
                            if board[x][y]: check[x][y] = 1
                        blocks.append((-count, -rainbow, -r, -c, t))
        if blocks:
            blocks.sort()
            return (-blocks[0][0], -blocks[0][2], -blocks[0][3], blocks[0][4])
        else:
            return 0

    def delete(a, b, t):
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        bfs = deque([(a, b)])
        while bfs:
            x, y = bfs.popleft()
            for k in range(4):
                nx = x + d[k][0]
                ny = y + d[k][1]
                if 0 <= nx < n and 0 <= ny < n and (board[nx][ny] == 0 or board[nx][ny] == t):
                    board[nx][ny] = -2
                    bfs.append((nx, ny))
        gravity()
        turn()
        return

    score = 0
    while True:
        target = find()
        if target:
            score += target[0] ** 2
            delete(target[1], target[2], target[3])
        else:
            print(score)
            break
    return
solution()