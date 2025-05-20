# 11946: ACM-ICPC
import sys
input = sys.stdin.readline
def solution():
    n, m, q = map(int, input().split())
    score = [[i, 0, 0] for i in range(1, n + 1)]
    solved = [[0] * (m + 1) for _ in range(n)]
    for _ in range(q):
        time, team, p, res = map(str, input().split())
        time = int(time)
        team = int(team) - 1
        p = int(p)
        if solved[team][p] == -1: continue
        elif res == 'AC':
            score[team][1] += 1
            score[team][2] += 20 * solved[team][p] + time
            solved[team][p] = -1
        else:
            solved[team][p] += 1
    score.sort(key = lambda x: (-x[1], x[2], x[0]))
    for i in range(n):
        print(*score[i])
solution()