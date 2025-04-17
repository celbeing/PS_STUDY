# 10215: Colored Bead Works
import sys
input = sys.stdin.readline
def solution():
    def left(board):
        new_board = [[0] * 4 for _ in range(4)]
        for i in range(4):
            k = 0
            for j in range(4):
                if board[i][j]:
                    new_board[i][k] = board[i][j]
                    k += 1
        return new_board

    def right(board):
        new_board = [[0] * 4 for _ in range(4)]
        for i in range(4):
            k = 3
            for j in range(3, -1, -1):
                if board[i][j]:
                    new_board[i][k] = board[i][j]
                    k -= 1
        return new_board

    def top(board):
        new_board = [[0] * 4 for _ in range(4)]
        for j in range(4):
            k = 0
            for i in range(4):
                if board[i][j]:
                    new_board[k][j] = board[i][j]
                    k += 1
        return new_board

    def bottom(board):
        new_board = [[0] * 4 for _ in range(4)]
        for j in range(4):
            k = 3
            for i in range(3, -1, -1):
                if board[i][j]:
                    new_board[k][j] = board[i][j]
                    k -= 1
        return new_board


    def search(now, board, final):
        c, t = 0, 0
        if now <= n:
            query = act[now]
            if query in 'LRTB':
                if query == 'L':
                    c, t = search(now + 1, left(board), final)
                elif query == 'R':
                    c, t = search(now + 1, right(board), final)
                elif query == 'T':
                    c, t = search(now + 1, top(board), final)
                else:
                    c, t = search(now + 1, bottom(board), final)
                return c, t
            else:
                next_case = []
                mask = [15, 8, 4, 12, 2, 10, 9, 8, 1, 6, 5, 4, 3, 2, 1, 0]
                cor = [(2, 2), (2, 1), (1, 2), (1, 1)]
                bm = 0
                if board[1][1]: bm += 8
                if board[1][2]: bm += 4
                if board[2][1]: bm += 2
                if board[2][2]: bm += 1
                for i in range(4):
                    if mask[bm] & 1 << i:
                        next_case.append(cor[i])

                if len(next_case) == 0:
                    for i in range(4):
                        for j in range(4):
                            if board[i][j] == 0:
                                next_case.append((i, j))
                for x, y in next_case:
                    board[x][y] = 1 if query == 'W' else 2
                    case, total = search(now + 1, board, final)
                    c += case
                    t += total
                    board[x][y] = 0
                return c, t
        else:
            if board == final:
                return 1, 1
            else:
                return 0, 1

    for _ in range(int(input())):
        board = [[0] * 4 for _ in range(4)]
        act = list(map(str, input().split()))
        n = int(act[0])
        final = [list(input().strip()) for _ in range(4)]
        for i in range(4):
            for j in range(4):
                if final[i][j] == 'E':
                    final[i][j] = 0
                elif final[i][j] == 'W':
                    final[i][j] = 1
                else:
                    final[i][j] = 2
        case, total = search(1, board, final)
        if total == 0:
            total += 1
            if board == final:
                case += 1
        print(case / total)
solution()