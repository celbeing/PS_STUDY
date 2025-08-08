import random
from heapq import heappush, heappop
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

def tri_cor(k):
    common_diff = 0
    level = 0
    count = 0
    while k > common_diff:
        k -= common_diff
        common_diff += 1
        level += 1
        count += 1
    return level, k

for tc in range(1, 101):
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    n = random.randint(1, 100000)
    t = random.randint(1, min(n, 100))
    while n in check:
        n = random.randint(1, 100000)
    w = file.writelines(f'{n} {t}')

    hq = []
    check_2 = []
    for _ in range(t):
        i = random.randint(1, n)
        j = random.randint(1, i)
        k = i - j + 1
        while True:
            for p, q in check_2:
                if j <= p and k <= q:
                    break
            else:
                check_2.append((j, k))
                break
            i = random.randint(1, n)
            j = random.randint(1, i)
            k = i - j + 1

        w = file.writelines(f'\n{j + k - 1} {j}')
        heappush(hq, (-j, -k))

    res = 0
    last = 0
    depth = 0
    while hq:
        j, k = heappop(hq)
        j, k = -j, -k
        if depth < k:
            res += depth * (last - j)
            last = j
            depth = k
    res += depth * last

    file = open(path + f'{tc}.out', 'w+', encoding = 'utf-8')
    w = file.writelines(f'{res}')