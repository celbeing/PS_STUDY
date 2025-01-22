# 18137: 나이트의 경로
import sys
input = sys.stdin.readline
def solution():
    k = []
    d = [(-1, -2), (-2, -1), (1, -2), (-2, 1), (2, -1), (-1, 2), (2, 1), (1, 2)]
    board = [[0] * 10000 for _ in range(10000)]
    def cor(x, y):
        t = x + y
        return (t - 1) * (t - 2) // 2 + y

    board[1][1] = 1
    k.append(1)
    x, y = 1, 1
    while True:
        for i in range(8):
            nx, ny = x + d[i][0], y + d[i][1]
            if nx <= 0 or ny <= 0 or board[nx][ny]: continue
            k.append(cor(nx, ny))
            board[nx][ny] = 1
            x, y = nx, ny
            break
solution()