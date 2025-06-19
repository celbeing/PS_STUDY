import random, math
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

def solution(n, edge):
    def dfs(now):
        dp[now] = 1
        for next in edge[now]:
            if dp[next]: continue
            dfs(next)
            dp[now] += dp[next]

    dp = [0] * (n + 1)

    dfs(1)

    node = 0
    high = 0
    for i in range(1, n + 1):
        res = 1
        for j in edge[i]:
            if dp[i] < dp[j]:
                res *= n - dp[i]
            else:
                res *= dp[j]
        if high < res:
            high = res
            node = i
    return node, high

path = r"C:\Users\kimsd\OneDrive\바탕 화면\tc\\"

s, e = 120, 120
check = set()
for tc in range(30, 31):
    n = 120
    edge = [[] for _ in range(n + 1)]
    for i in range(1, 117, 3):
        edge[i].append(i + 1)
        edge[i + 1].append(i + 2)
        edge[i + 2].append(120)
    edge[118].append(119)
    edge[119].append(120)

    file = open(path + f"{tc}.in", "w+", encoding='utf-8')
    w = file.writelines(f'{n}')
    '''
    n = random.randint(s, e)
    while n in check:
        n = random.randint(s, e)
    check.add(n)
    edge = [[] for _ in range(n + 1)]
    file = open(path + f"{tc}.in", "w+", encoding='utf-8')
    w = file.writelines(f'{n}')
    for i in range(2, n + 1):
        edge[i].append(random.randint(1, i - 1))
    '''
    shf = [i for i in range(1, n + 1)]
    random.shuffle(shf)
    edge_shf = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in edge[i]:
            a = shf[i - 1]
            b = shf[j - 1]
            edge_shf[a].append(b)
            edge_shf[b].append(a)
            w = file.writelines(f'\n{min(a, b)} {max(a, b)}')

    file = open(path + f"{tc}.out", "w+", encoding = 'utf-8')
    res, score = solution(n, edge_shf)
    w = file.writelines(f'{res} {score}')
