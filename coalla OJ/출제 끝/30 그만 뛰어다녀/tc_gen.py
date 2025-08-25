import random, solution

random.random()
inf = 1 << 31
mod = int(1e9) + 7

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
        t = random.randint(0, 1)
        if t:
            nx = random.randint(0, n - 1)
            while ground[nx][y] > -1 or nx == x:
                nx = random.randint(0, n - 1)
            ground[x][y] = abs(nx - x)
            x = nx
        else:
            ny = random.randint(0, m - 1)
            while ground[x][ny] > -1 or ny == y:
                ny = random.randint(0, m - 1)
            ground[x][y] = abs(ny - y)
            y = ny
    if ground[x][m - 1] == -1 and ground[n - 1][y] == -1:
        t = random.randint(0, 1)
        if t:
            ground[x][y] = m - 1 - y
            ground[x][m - 1] = n - 1 - x
        else:
            ground[x][y] = n - 1 - x
            ground[n - 1][y] = m - 1 - y
    elif ground[x][m - 1] == -1:
        ground[x][y] = m - 1 - y
        ground[x][m - 1] = n - 1 - x
    elif ground[n - 1][y] == -1:
        ground[x][y] = n - 1 - x
        ground[n - 1][y] = m - 1 - y
    else:
        finish = []
        for i in range(n):
            if i == x: continue
            if ground[i][y] == ground[i][m - 1] == -1:
                finish.append((1, i))
        for i in range(m):
            if i == y: continue
            if ground[x][i] == ground[n - 1][i] == -1:
                finish.append((0, i))
        random.shuffle(finish)
        t, i = finish.pop()
        if t:
            ground[x][y] = abs(x - i)
            ground[i][y] = n - 1 - i
            ground[i][m - 1] = m - 1 - y
        else:
            ground[x][y] = abs(y - i)
            ground[x][i] = m - 1 - i
            ground[m - 1][i] = n - 1 - x
    for i in range(n):
        for j in range(m):
            if ground[i][j] == -1:
                ground[i][j] = random.randint(0, max(n, m))


for tc in range(17, 21):
    n = random.randint(100, 100)
    m = random.randint(100, 100)
    ground = [[-1] * m for _ in range(n)]

    t = random.randint(0, 10)
    if t: perf_random()
    else: have_route()

    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    w = file.writelines(f'{n} {m}')
    for i in range(n):
        k = map(str, ground[i][:])
        w = file.writelines('\n')
        w = file.writelines(' '.join(k))


    file = open(path + f'{tc}.out', 'w+', encoding = 'utf-8')
    res = solution.solution(n, m, ground)
    if res:
        w = file.writelines(f'YES\n{res}')
    else:
        w = file.writelines(f'NO')
