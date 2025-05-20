# 7565: Ranking List
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    team = dict()
    for _ in range(n):
        team[input().strip()] = [0] * 12
    k, m = map(int, input().split())
    for _ in range(m):
        p, t, s, h = map(str, input().split())
        p = int(p)
        t = int(t)
        if team[h][p] <= 0:
            if s == "Yes":
                team[h][0] += t - team[h][p] * 20
                team[h][p] = 1
                team[h][-1] -= 1
            else:
                team[h][p] -= 1
    score_board = [(name, sc) for name, sc in team.items()]
    score_board.sort(key = lambda x: (x[1][-1], x[1][0], x[0]))
    rank = 1
    jump = 1
    print('{0:>2}. {1:<8}{2:>2}{3:>5}'.format(rank, score_board[0][0], -score_board[0][1][-1], score_board[0][1][0]))
    for i in range(1, n):
        if score_board[i][1][0] == score_board[i - 1][1][0] and score_board[i][1][-1] == score_board[i - 1][1][-1]:
            print('{0:>2}. {1:<8}{2:>2}{3:>5}'.format(rank, score_board[i][0], -score_board[i][1][-1],
                                                      score_board[i][1][0]))
            jump += 1
        else:
            rank += jump
            print('{0:>2}. {1:<8}{2:>2}{3:>5}'.format(rank, score_board[i][0], -score_board[i][1][-1],
                                                      score_board[i][1][0]))
            jump = 1
    print()


for _ in range(int(input())):
    solution()