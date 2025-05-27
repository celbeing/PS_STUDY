# 25478: Marinada
import sys
from collections import deque
input = sys.stdin.readline
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
inf = 10**9

n, m, k = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]
graph = [[inf] * (k + 2) for _ in range(k + 2)]
coord = [0] * (k + 2)
numbs = dict()
n_count = 1
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'N':
            coord[n_count] = (i, j)
            numbs[(i, j)] = n_count
            n_count += 1
        elif grid[i][j] == 'U':
            coord[0] = (i, j)
            numbs[(i, j)] = 0
        elif grid[i][j] == 'I':
            coord[-1] = (i, j)
            numbs[(i, j)] = k + 1

for i in range(k + 2):
    check = [[0] * m for _ in range(n)]
    bfs = deque([(0, coord[i][0], coord[i][1])])
    check[coord[i][0]][coord[i][1]] = 1

    while bfs:
        distance, x, y = bfs.popleft()
        if grid[x][y] != '.':
            j = numbs[(x, y)]
            graph[i][j] = distance

        for t in range(4):
            nx, ny = x + d[t][0], y + d[t][1]
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != '#' and check[nx][ny] == 0:
                check[nx][ny] = 1
                bfs.append((distance + 1, nx, ny))

for t in range(k + 2):
    graph[t][t] = 0
    for i in range(k + 2):
        for j in range(k + 2):
            graph[i][j] = min(graph[i][j], graph[i][t] + graph[t][j])

dp = [[0] * (1 << k + 1) for _ in range(k + 1)]
for i in range(1, k + 1):
    dp[i][-1] = graph[i][-1]

def tsp(now, visit):
    if dp[now][visit] == 0:
        dp[now][visit] = inf
        for next in range(1, k + 1):
            if visit & (1 << next): continue
            dp[now][visit] = min(dp[now][visit], tsp(next, visit | 1 << next) + graph[now][next])
    return dp[now][visit]

print(tsp(0, 1))