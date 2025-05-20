# 21922: 학부 연구생 민상
import sys
input = sys.stdin.readline
def solution():
    N, M = map(int, input().split())
    lab = [list(map(int, input().split())) for _ in range(N)]
    wind = [[0] * M for _ in range(N)]
    d = [0, (-1, 0), (0, 1), 0, (1, 0), 0, 0, 0, (0, -1)]
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 9:
                for k in range(4):
                    x, y = i, j
                    t = 1 << k
                    while 0 <= x < N and 0 <=  y < M and wind[x][y] & t == 0:
                        wind[x][y] |= t
                        if lab[x][y] == 1:
                            if t == 2: t = 8
                            elif t == 8: t = 2
                        elif lab[x][y] == 2:
                            if t == 1: t = 4
                            elif t == 4: t = 1
                        elif lab[x][y] == 3:
                            if t == 1: t = 2
                            elif t == 2: t = 1
                            elif t == 4: t = 8
                            else: t = 4
                        elif lab[x][y] == 4:
                            if t == 1: t = 8
                            elif t == 2: t = 4
                            elif t == 4: t = 2
                            else: t = 1
                        x += d[t][0]
                        y += d[t][1]
    seat = 0
    for i in range(N):
        for j in range(M):
            if wind[i][j]:
                seat += 1
    print(seat)
solution()