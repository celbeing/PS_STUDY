import random

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

for tc in range(1, 11):
    n = random.randint(10, 100)
    a = [random.randint(1, 100) for _ in range(n)]
    b = map(str, a)
    file = open(path + f"{tc}.in", "w+", encoding='utf-8')
    w = file.writelines(' '.join(b))
    k = random.randint(0, n - 1)
    w = file.writelines(f'\n{k}')
    file = open(path + f"{tc}.out", "w+", encoding = 'utf-8')
    w = file.writelines(f'{a[k]}')
