import random

path = r"C:\Users\kimsd\OneDrive\Documents\GitHub\PS_STUDY\coalla OJ\파이썬 컵\H\\"
for tc in range(1, 6):
    a = random.randint(100000000, 899999999)
    b = a + 100000000
    res = 0
    count = 0
    check = set()
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    for i in range(1, 10001):
        t = random.randint(a, b)
        w = file.writelines(f'{t}\n')
        if t in check and res == 0:
            res = t
            count = i
        check.add(t)

    file = open(path + f'{tc}.out', 'w+', encoding='utf-8')
    if res == 0:
        w = file.writelines(f'WIN\n')
        print('none')
    else:
        w = file.writelines(f'LOSE\n{count}\n{res}\n')