from random import randint
from collections import deque
check = set()
path = r"C:\Users\kimsd\OneDrive\Documents\GitHub\PS_STUDY\coalla OJ\2025 텍스트코딩 활용 문제\\"

for tc in range(31, 51):
    n = randint(2, 1000000)
    a = [randint(1, 9) for _ in range(n)]

    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    w = file.writelines(f'{n}\n{' '.join(map(str, a))}\n')

    count = 0
    part_sum = a[0]
    s, e = 0, 0
    while e < n:
        if part_sum > 10:
            part_sum -= a[s]
            s += 1
        elif part_sum < 10:
            e += 1
            if e == n: break
            part_sum += a[e]
        else:
            count += 1
            part_sum -= a[s]
            s += 1
            e += 1
            if e == n: break
            part_sum += a[e]

    file = open(path + f'{tc}.out', 'w+', encoding = 'utf-8')
    w = file.writelines(f'{count}\n')