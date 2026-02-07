from random import randint
from collections import deque
check = set()
path = r"C:\Users\kimsd\OneDrive\Documents\GitHub\PS_STUDY\coalla OJ\2025 텍스트코딩 활용 문제\\"
ls = 3000000 # 광속 = 초속 3억 미터

for tc in range(1, 51):
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    s = randint(1, 100)
    v = randint(1, 99)
    k = v * ls
    while (s, v) in check:
        s = randint(1, 100)
        v = randint(1, 99)
        k = v * ls
        check.add((s, v))
    res = s * k // 2

    w = file.writelines(f'{s} {v}\n')

    file = open(path + f'{tc}.out', 'w+', encoding = 'utf-8')
    w = file.writelines(f'{res}\n')