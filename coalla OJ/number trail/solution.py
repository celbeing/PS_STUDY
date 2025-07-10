import sys
input = sys.stdin.readline
d = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def dfs(x, y, c):
    if c == fin:
        return 1

    t = c
    while t <= fin and not(t in loc):
        t += 1
    if t <= fin:
        dist = abs(loc[t][0] - x) + abs(loc[t][1] - y)
        if (dist & 1 ^ (t - c) & 1) or dist > t - c: return 0

    for a, b in d:
        dx, dy = x + a, y + b
        if 0 <= dx < n and 0 <= dy < n:
            if board[dx][dy] == 0:
                board[dx][dy] = c + 1
                if dfs(dx, dy, c + 1): return 1
                board[dx][dy] = 0
            elif board[dx][dy] == c + 1:
                if dfs(dx, dy, c + 1): return 1
    return 0

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
fin = n * n

loc = {}
for i in range(n):
    for j in range(n):
        if board[i][j]:
            loc[board[i][j]] = (i, j)
res = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 0:
            board[i][j] = 1
            res = dfs(i, j, 1)
            if res: break
            board[i][j] = 0
        elif board[i][j] == 1:
            res = dfs(i, j, 1)
            if res: break
    if res: break

if res:
    print('YES')
    for b in board:
        print(*b)
else:
    print('NO')