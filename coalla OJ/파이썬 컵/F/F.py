import random

def gcd(a: int, b: int):
    while b:
        a, b = b, a % b
    return a

path = r"C:\Users\kimsd\OneDrive\Documents\GitHub\PS_STUDY\coalla OJ\파이썬 컵\F\\"
for tc in range(1, 31):
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    a = random.randint(2, 250)
    b = random.randint(2, 250)
    w = file.writelines(f'{a} {b}\n')

    lcm = a * b // gcd(a, b)
    file = open(path + f'{tc}.out', 'w+', encoding='utf-8')
    w = file.writelines(f'{lcm}\n')