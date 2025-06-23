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

path = r"C:\Users\kimsd\OneDrive\바탕 화면\tc\\"

def perf_random():
    for i in range(n):
        for j in range(m):
            k = random.randint(1, 100)
            if k <= 80: ground[i][j] = random.randint(1, 5)
            elif k <= 88: ground[i][j] = random.randint(6, 8)
            elif k <= 93: ground[i][j] = random.randint(9, 10)
            elif k <= 95: ground[i][j] = random.randint(11, 15)
            elif k <= 96: ground[i][j] = random.randint(16, 50)
            else: ground[i][j] = 0

def have_route():
    p = random.randint(1, (n * m // 2) - 1)
    x, y = 0, 0
    for _ in range(p):
        nx, ny = random.randint(0, n - 1), random.randint(0, n - 1)
        while ground[nx][ny] != -1 or (ground[x][ny] > -1 and ground[nx][y] > -1) or x == nx or y == ny:
            nx, ny = random.randint(0, n - 1), random.randint(0, n - 1)


for tc in range(11, 21):
    n = random.randint(2, 20)
    m = random.randint(2, 20)
    ground = [[-1] * m for _ in range(n)]


    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    w = file.writelines(f'{n} {m}')
    for i in range(n):
        k = map(str, ground[i][:])
        w = file.writelines('\n')
        w = file.writelines(' '.join(k))

    check = [[0] * m for _ in range(n)]
    check[0][0] = 1
    bfs = deque([(0, 0, 0)])
    possible = False
    s = 0
    while bfs:
        x, y, step = bfs.popleft()
        if x == n - 1 and y == m - 1:
            possible = True
            s = step
            break
        k = ground[x][y]
        for dx in (x + k, x - k):
            for dy in (y + k, y - k):
                if 0 <= dx < n and 0 <= dy < m and check[dx][dy] == 0:
                    check[dx][dy] = 1
                    bfs.append((dx, dy, step + 1))
    file = open(path + f'{tc}.out', 'w+', encoding = 'utf-8')
    if possible:
        w = file.writelines(f'YES\n{s}')
    else:
        w = file.writelines(f'NO')
