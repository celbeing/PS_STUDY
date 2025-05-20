# 16197: 두 동전
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    N, M = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(N)]
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    coin = []
    wall = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] == '#':
                wall[i][j] = 1
            elif board[i][j] == 'o':
                coin.append((i, j))
    bfs = deque([(coin[0], coin[1], 0)])
    while bfs:
        a, b, k = bfs.popleft()
        if k == 10: continue
        for i in range(4):
            drop_a, drop_b = False, False
            adx = a[0] + d[i][0]
            ady = a[1] + d[i][1]
            bdx = b[0] + d[i][0]
            bdy = b[1] + d[i][1]

            if not (0 <= adx < N and 0 <= ady < M): drop_a = True
            if not (0 <= bdx < N and 0 <= bdy < M): drop_b = True
            if drop_a ^ drop_b:
                print(k + 1)
                exit()
            elif drop_a:
                continue
            else:
                if wall[adx][ady]:
                    adx, ady = a[0], a[1]
                    if adx == bdx and ady == bdy:
                        bdx, bdy = b[0], b[1]
                    elif wall[bdx][bdy]:
                        bdx, bdy = b[0], b[1]
                elif wall[bdx][bdy]:
                    bdx, bdy = b[0], b[1]
                    if bdx == adx and bdy == ady:
                        adx, ady = a[0], a[1]
                    elif wall[adx][ady]:
                        adx, ady = a[0], a[1]
                bfs.append(((adx, ady), (bdx, bdy), k + 1))
    print(-1)
solution()