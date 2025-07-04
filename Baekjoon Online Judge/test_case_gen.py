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
for tc in range(1, 11):
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    a, b = random.randint(1, 20), random.randint(1, 20)
    if (a, b) in check:
        a, b = random.randint(1, 20), random.randint(1, 20)
        check.add((a, b))
    w = file.writelines(f'{a} {b}')
    file = open(path + f'{tc}.out', 'w+', encoding = 'utf-8')

    if a > b:
        a, b = b, a
    if b - a > 1:
        w = file.writelines(f'{a + 1}')
    for k in range(a + 2, b):
        w = file.writelines(f'\n{k}')