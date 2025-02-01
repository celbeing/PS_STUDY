# 3025: 돌 던지기
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    r, c = map(int, input().split())
    board = [list(input().strip()) for _ in range(r)]
    route = [deque() for _ in range(c)]

    def drop(C):
        x, y = 0, C
        if route[C]:
            x, y = route[C].pop()
            while route[C] and board[x][y] != '.':
                x, y = route[C].pop()
            if not route[C]:
                x, y = 0, C
                while x < r and board[x][y] == '.': x += 1
                x -= 1
        else:
            while x < r and board[x][y] == '.': x += 1
            x -= 1

        while True:
            left = y - 1
            right = y + 1
            bottom = x + 1
            if bottom < r and board[bottom][y] == 'O':
                if left >= 0 and board[x][left] == board[bottom][left] == '.':
                    route[C].append((x, y))
                    x += 1
                    y -= 1
                    while x < r and board[x][y] == '.': x += 1
                    x -= 1
                elif right < c and board[x][right] == board[bottom][right] == '.':
                    route[C].append((x, y))
                    x += 1
                    y += 1
                    while x < r and board[x][y] == '.': x += 1
                    x -= 1
                else: break
            else: break
        board[x][y] = 'O'
        if not(route[C] and route[C][-1][0] + 1 == x):
            route[C].append((x - 1, y))
        return

    for _ in range(int(input())):
        C = int(input())
        drop(C - 1)

    for line in board:
        print(''.join(line))
    return
solution()