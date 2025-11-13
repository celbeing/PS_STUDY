import random

path = r"C:\Users\kimsd\OneDrive\Documents\GitHub\PS_STUDY\coalla OJ\파이썬 컵\B\\"

for tc in range(1, 31):
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    c = random.randint(1, 100)
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    w = file.writelines(f'{a} {b} {c}\n')
    file = open(path + f'{tc}.out', 'w+', encoding='utf-8')
    w = file.writelines(f'{c}\n{b}\n{a}\n')