# 10215: Colored Bead Works
import sys
input = sys.stdin.readline
def solution():
    def top(board):
        for i in range(4):
            for j in range(4):
                if board[i][j] == 0:
                    for k in range(j + 1, 4):
                        if board[i][k]:
                            board[i][j] = board[i][k]
                            board[i][k] = 0
        return board

    def bottom(board):
        for i in range(4):
            for j in range(3, -1, -1):
                if board[i][j] == 0:
                    for k in range(j - 1, -1, -1):
                        if board[i][k]:
                            board[i][j] = board[i][k]
                            board[i][k] = 0
        return board

    def left(board):
        for i in range(4):
            for j in range(4):
                if board[i][j] == 0:
                    for k in range(i + 1, 4):
                        if board[k][j]:
                            board[i][j] = board[k][j]
                            board[k][j] = 0
        return board

    def right(board):
        for i in range(3, -1, -1):
            for j in range(4):
                if board[i][j] == 0:
                    for k in range(i - 1, -1, -1):
                        if board[k][j]:
                            board[i][j] = board[k][j]
                            board[k][j] = 0
        return board

    def

    for _ in range(int(input())):
        board = [[0] * 4 for _ in range(4)]
        case = [0, 0]
        act = list(map(str, input().split()))[1:]
        final = [list(input().strip()) for _ in range(4)]
        for i in range(4):
            for j in range(4):
                if final[i][j] == 'E':
                    final[i][j] = 0
                elif final[i][j] == 'W':
                    final[i][j] = 1
                else:
                    final[i][j] = 2
        if case[1] == 0:
            if
        print(case[0] / case[1])