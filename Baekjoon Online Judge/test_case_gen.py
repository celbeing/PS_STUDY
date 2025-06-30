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
for tc in range(1, 10):
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    k = tc
    w = file.writelines(f'{k}')
    for i in range(1, k):
        w = file.writelines(f'\n{i} {i + 1}')
    res = k - 1
    t = 1
    for i in range(1, k // 2 + 1):
        if i * (k - 1 - i) > res:
            res = i * (k - 1 - i)
            t = i + 1
    file = open(path + f'{tc}.out', 'w+', encoding = 'utf-8')
    w = file.writelines(f'{t} {res}')