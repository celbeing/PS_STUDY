# 7565: Rankin List
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
    print(score_board)

for _ in range(int(input())):
    solution()