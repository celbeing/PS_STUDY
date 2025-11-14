import random

check = set()
path = r"C:\Users\kimsd\OneDrive\Documents\GitHub\PS_STUDY\coalla OJ\파이썬 컵\K\\"
for tc in range(1, 31):
    n = random.randint(1, 100000)
    while n in check:
        n = random.randint(1, 100000)
    check.add(n)
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    w = file.writelines(f'{n}\n')

    tri = []
    while n > 0:
        tri.append(n % 3)
        n //= 3

    res = 0
    while tri:
        res *= 10
        res += tri.pop()
    file = open(path + f'{tc}.out', 'w+', encoding='utf-8')
    w = file.writelines(f'{res}\n')