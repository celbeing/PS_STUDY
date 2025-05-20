#6229: Bronze Lilypad Pond
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    N, M, a, b = map(int, input().split())
    d = [(a,b),(a,-b),(-a,b),(-a,-b),(b,a),(b,-a),(-b,a),(-b,-a)]
    field = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0] * M for _ in range(N)]
    bfs = deque([])
    for i in range(N):
        for j in range(M):
            if field[i][j] == 3:
                bfs.append((i,j))
                visit[i][j] = 1
                break
        if bfs: break

    while bfs:
        x, y = bfs.popleft()
        if field[x][y] == 4:
            print(visit[x][y] - 1)
            break
        for i in range(8):
            dx = d[i][0] + x
            dy = d[i][1] + y
            if 0 <= dx < N and 0 <= dy < M and visit[dx][dy] == 0 and (field[dx][dy] == 1 or field[dx][dy] == 4):
                bfs.append((dx,dy))
                visit[dx][dy] = visit[x][y] + 1
solution()