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

'''
from bisect import bisect_right as bi
from bisect import bisect_left as bi_l
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
def solution():
    r, c = map(int, input().split())
    board = [list(input().strip()) for _ in range(r)]
    top = [deque([]) for _ in range(c)]
    for j in range(c):
        flag = True
        for i in range(r):
            if board[i][j] == '.': flag = True
            elif flag:
                flag = False
                top[j].append(i - 1)
        top[j].append(r - 1)

    def drop(R, C):
        left = C - 1
        right = C + 1
        bottom = R + 1

        # 왼쪽으로 미끄러질 수 있는가?
        # 조건1: 왼쪽 열이 0번 이상
        # 조건2: 아래 행이 R번 미만
        # 조건3: 왼쪽 칸이 빈칸
        # 조건4: 왼쪽 아래 칸이 빈칸
        if left >= 0 and bottom < r and board[bottom][C] == 'O' and board[R][left] == '.' and board[bottom][left] == '.':
            drop(top[left][bi(top[left], R)], left)

        elif right < c and bottom < r and board[bottom][C] == 'O' and board[R][right] == '.' and board[bottom][right] == '.':
            drop(top[right][bi(top[right], R)], right)

        else:
            board[R][C] = 'O'
            top[C][bi_l(top[C], R)] -= 1
        return

    for _ in range(int(input())):
        C = int(input()) - 1
        drop(top[C][0], C)
    for line in board:
        print(''.join(line))
    return
solution()
'''