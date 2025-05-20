# 9840: Lazycat
import sys
from collections import deque
input = sys.stdin.readline

inf = 10_000
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
n = int(input())
field = [list(input().strip()) for _ in range(n)]

number = dict()
location = [(0, 0)]
food_count = 1
sx, sy, bx, by = 0, 0, 0, 0
for i in range(n):
    for j in range(n):
        if field[i][j] == 'S':
            sx, sy = i, j
            number[(sx, sy)] = 0
            location[0] = (sx, sy)
        elif field[i][j] == 'B':
            bx, by = i, j
        elif field[i][j] == 'F':
            number[(i, j)] = food_count
            location.append((i, j))
            food_count += 1
number[(bx, by)] = food_count
location.append((bx, by))
dist = [[inf] * (food_count + 1) for _ in range(food_count + 1)]
for i in range(food_count):
    x, y = location[i]
    check = [[0] * n for _ in range(n)]
    bfs = deque([(x, y)])
    check[x][y] = 1
    roop_count = 1
    distance = 1
    while bfs:
        next_step = 0
        for _ in range(roop_count):
            x, y = bfs.popleft()
            for k in range(4):
                dx, dy = x + d[k][0], y + d[k][1]
                if 0 <= dx < n and 0 <= dy < n and check[dx][dy] == 0 and field[dx][dy] != 'X':
                    check[dx][dy] = 1
                    next_step += 1
                    if field[dx][dy] != '0':
                        j = number[(dx, dy)]
                        dist[i][j] = distance
                        dist[j][i] = distance
                    bfs.append((dx, dy))
        roop_count = next_step
        distance += 1

dp = [[0] * (1 << food_count) for _ in range(food_count)]
for i in range(food_count):
    dp[i][(1 << food_count) - 1] = dist[i][food_count]

def TSP(now, visit):
    if dp[now][visit] == 0:
        dp[now][visit] = inf
        for i in range(food_count):
            if dist[now][i] == inf or visit & (1 << i): continue
            dp[now][visit] = min(dp[now][visit], TSP(i, visit | 1 << i) + dist[now][i])
    return dp[now][visit]

res = TSP(0, 1)

if res >= inf: print(-1)
else: print(res)