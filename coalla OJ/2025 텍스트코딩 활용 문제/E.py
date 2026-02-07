from random import randint
from collections import deque
check = set()
path = r"C:\Users\kimsd\OneDrive\Documents\GitHub\PS_STUDY\coalla OJ\2025 텍스트코딩 활용 문제\\"
sieve = [1] * 10001
prime = []
for i in range(2, 10001):
    if sieve[i]:
        prime.append(i)
        for j in range(i * i, 10001, i):
            sieve[j] = 0
print('prime found')

for tc in range(1, 51):
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    a, b, a_idx, b_idx = 0, 0, 0, 0
    while True:
        a = randint(1, 10000)
        b = randint(a + 1, 10001)
        a_idx, b_idx = 0, 0

        s, e = 0, len(prime)
        while s < e:
            m = (s + e) // 2
            if prime[m] < a:
                s = m + 1
            else:
                e = m
        a_idx = s

        s, e = 0, len(prime)
        while s < e:
            m = (s + e) // 2
            if prime[m] < b:
                s = m + 1
            else:
                e = m
        b_idx = s

        if not((a, b) in check) and b_idx - a_idx > 1:
            break
    new_prime = prime[a_idx:b_idx]
    k = randint(1, len(new_prime))

    w = file.writelines(f'{a} {b} {k}\n')

    file = open(path + f'{tc}.out', 'w+', encoding = 'utf-8')
    w = file.writelines(f'{new_prime[k - 1]}')
