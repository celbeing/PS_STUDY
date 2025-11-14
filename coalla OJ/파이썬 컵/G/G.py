import random

path = r"C:\Users\kimsd\OneDrive\Documents\GitHub\PS_STUDY\coalla OJ\파이썬 컵\G\\"
for tc in range(1, 11):
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    n = random.randint(10, 50)
    a = [random.randint(1, 10) for _ in range(n)]
    w = file.writelines(f'{n}\n')
    for i in range(n - 1):
        w = file.writelines(f'{a[i]} ')
    w = file.writelines(f'{a[-1]}\n')

    res = 0
    for i in range(n):
        l, r = 0, 0
        for j in range(i - 1, -1, -1):
            if a[j] >= a[i]:
                l = i - j - 1
                break
        for j in range(i + 1, n):
            if a[j] >= a[i]:
                r = j - i - 1
                break
        if res < max(l, r):
            res = max(l, r)
    file = open(path + f'{tc}.out', 'w+', encoding='utf-8')
    w = file.writelines(f'{res}\n')