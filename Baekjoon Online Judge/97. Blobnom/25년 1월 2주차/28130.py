# 28130: 슈넬치킨 랑데부
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    n, m = map(int, input().split())
    cycle = (n + m - 2) << 1
    ground = [list(input().rstrip()) for _ in range(n)]
    sw = []
    bfs = deque()
    check = [[-1] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if ground[i][j] == 'A':
                bfs.append((i, j))
                check[i][j] = 0
            elif ground[i][j] == 'B':
                sw = [i, j]
            elif ground[i][j] == 'G':
                check[i][j] = 0

    while bfs:
        nx, ny = bfs.popleft()
        for dir in range(4):
            dx, dy = nx + d[dir][0], ny + d[dir][1]
            if 0 <= dx < n and 0 <= dy < m and check[dx][dy] == -1:
                check[dx][dy] = check[nx][ny] + 1
                bfs.append((dx, dy))
    time = 0
    r = int(1e9)
    for _ in range(cycle):
        time += 1
        if sw[0] == 0 and sw[1] < m - 1:
            sw[1] += 1
        elif sw[0] < n - 1 and sw[1] == m - 1:
            sw[0] += 1
        elif sw[0] == n - 1 and sw[1] > 0:
            sw[1] -= 1
        else:
            sw[0] -= 1
        sh = check[sw[0]][sw[1]]
        sunwoo = time
        while r > sunwoo < sh: sunwoo += cycle
        if sh < 0 or (sh - time) & 1: continue
        r = min(r, sunwoo)
    if r == int(1e9): print(-1)
    else: print(r)
    return
solution()