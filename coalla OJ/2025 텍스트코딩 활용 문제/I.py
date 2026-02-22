from random import randint
from collections import deque
check = set()
path = r"C:\Users\kimsd\OneDrive\Documents\GitHub\PS_STUDY\coalla OJ\2025 텍스트코딩 활용 문제\\"

for tc in range(1, 51):
    n = randint(2, 10)
    cost = [0, 1]
    for _ in range(n - 1):
        t = randint(1, 100)
        while t in cost:
            t = randint(1, 100)
        cost.append(t)
    cost.sort()
    c = randint(1, 100000)

    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    w = file.writelines(f'{n} {c}\n')
    w = file.writelines(f'{' '.join(map(str, cost[1:]))}\n')

    dp = [[0] * (c + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(cost[i]):
            dp[i][j] = dp[i - 1][j]
        for j in range(cost[i], c + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - cost[i]]
            dp[i][j] %= 1_000_000_009

    file = open(path + f'{tc}.out', 'w+', encoding = 'utf-8')
    w = file.writelines(f'{dp[n][c]}\n')