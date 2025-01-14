# 28130: 슈넬치킨 랑데부
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    n, m = map(int, input().split())
    ground = [list(input().rstrip()) for _ in range(n)]
    sw = (0, 0)
    sh = deque()
    for i in range(n):
        for j in range(m):
            if ground[i][j] == 'A':
                sh.append((i, j))
            elif ground[i][j] == 'B':
                sw = (i, j)
    if (abs(sh[0][0] - sw[0]) + abs(sh[0][1] - sw[1])) & 1:
        print(-1)
        return
    time = 0
    while sh:
        if sw in sh: break
        k = len(sh)
        check = [[0] * m for _ in range(n)]
        for _ in range(k):
            nx, ny = sh.popleft()
            for dir in range(4):
                dx = nx + d[dir][0]
                dy = ny + d[dir][1]
                if 0 <= dx < n and 0 <= dy < m and ground[dx][dy] != 'G' and check[dx][dy] == 0:
                    check[dx][dy] = 1
                    sh.append((dx, dy))

        x, y = sw
        if x == 0 and y < m - 1:
            y += 1
        elif x < n - 1 and y == m - 1:
            x += 1
        elif x == n - 1 and y > 0:
            y -= 1
        else:
            x -= 1
        sw = (x, y)

        time += 1
    if sw in sh:
        print(time)
    else:
        print(-1)
    return
solution()