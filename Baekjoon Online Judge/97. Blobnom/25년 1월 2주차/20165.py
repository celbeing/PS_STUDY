# 20165: 인내의 도미노 장인 호석
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n, m, r = map(int, input().split())
    d = {'E': (0, 1), 'W': (0, -1), 'S': (1, 0), 'N': (-1, 0)}
    board = [list(map(int, input().split())) for _ in range(n)]
    check = [['S'] * m for _ in range(n)]
    domino = deque()
    score = 0
    for _ in range(r):
        x, y, dir = map(str, input().split())
        x = int(x) - 1; y = int(y) - 1
        if check[x][y] == 'S':
            domino.append((x, y))
            check[x][y] = 'F'
            count = 1
            while domino:
                nx, ny = domino.popleft()
                for i in range(1, board[nx][ny]):
                    dx, dy = nx + d[dir][0] * i, ny + d[dir][1] * i
                    if 0 <= dx < n and 0 <= dy < m and check[dx][dy] == 'S':
                        domino.append((dx, dy))
                        check[dx][dy] = 'F'
                        count += 1
            score += count

        x, y = map(int, input().split())
        check[x - 1][y - 1] = 'S'

    print(score)
    for line in check:
        print(*line)
solution()