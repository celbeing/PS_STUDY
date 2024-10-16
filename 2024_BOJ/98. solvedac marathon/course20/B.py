#6229: Bronze Lilypad Pond
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    N, M, a, b = map(int, input().split())
    d1 = [(a,0),(0,a),(-a,0),(0,-a)]
    d2 = [(b,b),(b,-b),(-b,b),(-b,-b)]
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
        for i in range(4):
            dx = d1[i][0] + x
            dy = d1[i][1] + y
            for j in range(4):
                tx = d2[j][0] + dx
                ty = d2[j][1] + dy
                if 0 <= tx < N and 0 <= ty < M and visit[tx][ty] == 0 and (field[tx][ty] == 1 or field[tx][ty] == 4):
                    bfs.append((tx,ty))
                    visit[tx][ty] = visit[x][y] + 1
solution()