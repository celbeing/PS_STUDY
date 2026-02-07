from random import randint
from collections import deque
check = set()
path = r"C:\Users\kimsd\OneDrive\Documents\GitHub\PS_STUDY\coalla OJ\2025 텍스트코딩 활용 문제\\"

for tc in range(1, 51):
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    k = randint(2, 100)
    a = 0
    while True:
        a += randint(1, 9)
        for _ in range(k - 1):
            a *= 10
            a += randint(0, 9)
        if not(a in check):
            check.add(a)
            break
    w = file.writelines(f'{k}\n{a}\n')

    small = a
    large = a
    t = 10 ** (k - 1)
    for i in range(k - 1):
        tmp = a // t
        a %= t
        a *= 10
        a += tmp
        if a > large: large = a
        elif a < small: small = a

    file = open(path + f'{tc}.out', 'w+', encoding = 'utf-8')
    w = file.writelines(f'{large-small}\n')