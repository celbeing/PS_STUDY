import random
from collections import deque

random.random()
inf = 1 << 31
mod = int(1e9) + 7

def euc(a, b):
    while b:
        a, b = b, a % b
    return a

def eratos_sieve():
    sieve = [0] * 10001
    sieve[0] = 1
    sieve[1] = 1
    prime = []
    for i in range(2, 10001):
        if sieve[i]: continue
        prime.append(i)
        for j in range(i * i, 10001, i):
            sieve[j] = 1

check = set()
path = r"C:\Users\kimsd\OneDrive\바탕 화면\tc\\"
d = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def dfs(x, y, c):
    if c == fin:
        return 1

    t = c
    while t <= fin and not(t in loc):
        t += 1
    if t <= fin:
        dist = abs(loc[t][0] - x) + abs(loc[t][1] - y)
        if dist != t - c: return 0

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

for tc in range(11, 16):
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    n = int(input())
    fin = n * n
    w = file.writelines(f'{n}')
    board = []
    for _ in range(n):
        line = input().strip()
        w = file.writelines(f'\n{line}')
        board.append(list(map(int, line.split())))
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

    file = open(path + f'{tc}.out', 'w+', encoding = 'utf-8')
    if res:
        w = file.writelines(f'YES')
        for i in range(n):
            line = str(board[i][0])
            for j in range(1, n):
                line += f' {str(board[i][j])}'
            w = file.writelines(f'\n{line}')
    else:
        w = file.writelines(f'NO')