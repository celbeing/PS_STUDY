import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
desk = [list(map(int, input().split())) for _ in range(n)]
check = [[0] * m for _ in range(n)]
check[0][0] = 1
bfs = deque([(0, 0, 0)])
res = 0
while bfs:
    x, y, step = bfs.popleft()
    if x == n - 1 and y == m - 1:
        res = step
        break
    k = desk[x][y]
    for dx, dy in [(x + k, y), (x, y + k), (x - k, y), (x, y - k)]:
        if 0 <= dx < n and 0 <= dy < m and check[dx][dy] == 0:
            check[dx][dy] = 1
            bfs.append((dx, dy, step + 1))

print(f'YES\n{res}' if res else 'NO')

'''
def solution(n, m, ground):
    check = [[0] * m for _ in range(n)]
    check[0][0] = 1
    bfs = deque([(0, 0, 0)])
    s = 0
    while bfs:
        x, y, step = bfs.popleft()
        if x == n - 1 and y == m - 1:
            s = step
            break
        k = ground[x][y]
        for dx, dy in ((x + k, y), (x, y + k), (x - k, y), (x, y - k)):
            if 0 <= dx < n and 0 <= dy < m and check[dx][dy] == 0:
                check[dx][dy] = 1
                bfs.append((dx, dy, step + 1))
    return s
'''