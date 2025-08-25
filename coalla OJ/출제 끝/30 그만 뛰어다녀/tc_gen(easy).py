import random
from collections import deque

random.random()
inf = 1 << 31
mod = int(1e9) + 7

path = r"C:\Users\kimsd\OneDrive\바탕 화면\tc\\"

for tc in range(1, 11):
    n = random.randint(10, 100)
    ground = [random.randint(1, 10) for _ in range(n)]
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    w = file.writelines(f'1 {n}\n')
    k = map(str, ground[:])
    w = file.writelines(' '.join(k))

    file = open(path + f'{tc}.out', 'w+', encoding = 'utf-8')
    check = [-1] * n
    check[0] = 0
    bfs = deque([0])
    while bfs:
        now = bfs.popleft()
        if now == n - 1: break
        for next in (now + ground[now], now - ground[now]):
            if 0 <= next < n and check[next] == -1:
                check[next] = check[now] + 1
                bfs.append(next)

    if check[n - 1] == -1:
        w = file.writelines(f'NO')
    else:
        w = file.writelines(f'YES\n{check[n - 1]}')
