import random
from math import floor, ceil
random.random()
check = set()
path = r"C:\Users\kimsd\OneDrive\Documents\GitHub\PS_STUDY\coalla OJ\기초과정 연습문제\07.버림\\"

for tc in range(1, 51):
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    a = random.randint(1, 100000)
    b = random.randint(1, a)
    while (a, b) in check:
        a = random.randint(1, 100000)
        b = random.randint(1, a)
    check.add((a, b))
    w = file.writelines(f'{a}\n{b}\n')

    a //= b

    file = open(path + f'{tc}.out', 'w+', encoding = 'utf-8')
    w = file.writelines(f'{a}\n')