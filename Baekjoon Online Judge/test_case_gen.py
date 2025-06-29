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

for tc in range(10, 21):
    h = random.randint(0, 23)
    m = random.randint(0, 59)
    s = random.randint(0, 59)
    q = random.randint(10000, 86400)
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    w = file.writelines(f'{h:02d}:{m:02d}:{s:02d}\nshutdown -s -t {q}')

    h += q // 3600
    q %= 3600
    m += q // 60
    q %= 60
    s += q
    if s >= 60:
        s %= 60
        m += 1
    if m >= 60:
        m %= 60
        h += 1
    h %= 24
    file = open(path + f'{tc}.out', 'w+', encoding = 'utf-8')
    w = file.writelines(f'{h:02d}:{m:02d}:{s:02d}')