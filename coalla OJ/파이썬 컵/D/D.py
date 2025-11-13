import random

path = r"C:\Users\kimsd\OneDrive\Documents\GitHub\PS_STUDY\coalla OJ\파이썬 컵\D\\"

for tc in range(1, 31):
    a = random.randint(10, 999)
    b = random.randint(10, 999)
    c = random.randint(10, 999)
    d = random.randint(5, 10)
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    w = file.writelines(f'{a} {b} {c} {d}\n')
    file = open(path + f'{tc}.out', 'w+', encoding='utf-8')
    w = file.writelines(f'{(a // d) * (b // d) * (c // d)}\n')