import random

check = set()
path = r"C:\Users\kimsd\OneDrive\Documents\GitHub\PS_STUDY\coalla OJ\파이썬 컵\J\\"
for tc in range(1, 31):
    n = random.randint(2, 100000)
    while n in check:
        n = random.randint(2, 100000)
    check.add(n)
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    w = file.writelines(f'{n}\n')

    d = 0
    for i in range(1, n):
        if n % i == 0:
            d += i

    file = open(path + f'{tc}.out', 'w+', encoding='utf-8')
    w = file.writelines(f'{'부족수' if d < n else ('과잉수' if d > n else '완전수')}\n')

    if d == n: print('완전수!!!!!!!!')
    elif d < n: print('부족수')
    else: print('과잉수')