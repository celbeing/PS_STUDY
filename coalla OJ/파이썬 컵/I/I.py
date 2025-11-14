import random

path = r"C:\Users\kimsd\OneDrive\Documents\GitHub\PS_STUDY\coalla OJ\파이썬 컵\I\\"
for tc in range(1, 6):
    cand = dict()
    res = 0
    high = 0
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    for i in range(100001):
        n = random.randint(1, 999999999)
        if n in cand:
            cand[n] += 1
        else:
            cand[n] = 1
        if high < cand[n]:
            high = cand[n]
            res = n
        w = file.writelines(f'{n}\n')

    file = open(path + f'{tc}.out', 'w+', encoding='utf-8')
    w = file.writelines(f'{res}\n{high}\n')