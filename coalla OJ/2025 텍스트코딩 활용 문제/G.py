from random import randint
from collections import deque
check = set()
path = r"C:\Users\kimsd\OneDrive\Documents\GitHub\PS_STUDY\coalla OJ\2025 텍스트코딩 활용 문제\\"

for tc in range(31, 51):
    n = randint(2, 1000)
    a = [randint(1, 100000) for _ in range(n)]
    b = randint(n, max(n, int(sum(a) * 0.8)))
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    w = file.writelines(f'{n} {b}\n')
    w = file.writelines(f'{' '.join(map(str, a))}\n')

    file = open(path + f'{tc}.out', 'w+', encoding = 'utf-8')
    s, e = 1, max(a)
    while s < e:
        m = (s + e + 1) // 2
        expc = 0
        for k in a:
            expc += m if k > m else k
        if expc <= b: s = m
        else: e = m - 1

    w = file.writelines(f'{s}\n')