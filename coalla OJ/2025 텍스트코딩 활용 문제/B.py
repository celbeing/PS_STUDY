import random, sys
from collections import deque
check = set()
path = r"C:\Users\kimsd\OneDrive\Documents\GitHub\PS_STUDY\coalla OJ\2025 텍스트코딩 활용 문제\\"
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for tc in range(1, 51):
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    m = random.randint(1, 12)
    d = random.randint(1, month[m])
    while (m, d) in check:
        m = random.randint(1, 12)
        d = random.randint(1, month[m])
    w = file.writelines(f'{m} {d}\n')

    file = open(path + f'{tc}.out', 'w+', encoding = 'utf-8')
    t = (sum(month[:m]) + d) % 7
    w = file.writelines(f'{'수목금토일월화'[t]}\n')