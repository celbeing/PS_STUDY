# 28130: 슈넬치킨 랑데부
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    n, m = map(int, input().split())
    ground = [list(input().rstrip()) for _ in range(n)]
    time = [[-1] * m for _ in range(n)]
    for i in range(m):
        time[0][i] = i
    for i in range(1, n):
        time[i][-1] = time[0][-1] + i
    for i in range(1, m):
        time[-1][-(i + 1)] = time[-1][-1] + i
    for i in range(1, n - 1):
        time[-(i + 1)][0] = time[-1][0] + i
    bfs = deque()
    sh = (0, 0)
    sw = (0, 0)
    for i in range(n):
        for j in range(m):
            if ground[i][j] == 'A':
                bfs.append((i, j))
                sh = (i, j)
            elif ground[i][j] == 'B':
                sw = (i, j)
            elif ground[i][j] == 'G':
                time[i][j] = 0
