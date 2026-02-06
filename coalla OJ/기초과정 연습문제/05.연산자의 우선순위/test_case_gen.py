import random
random.random()
check = set()
path = r"C:\Users\kimsd\OneDrive\Documents\GitHub\PS_STUDY\coalla OJ\기초과정 연습문제\05.연산자의 우선순위\\"

for tc in range(1, 51):
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 5)
    d = random.randint(2, 10)
    while (a, b, c, d) in check:
        a = random.randint(1, 50)
        b = random.randint(1, 50)
        c = random.randint(1, 10)
        d = random.randint(2, 10)
    check.add((a, b, c, d))
    w = file.writelines(f'{a}\n{b}\n{c}\n{d}\n')

    a += b
    a **= c
    a //= d

    file = open(path + f'{tc}.out', 'w+', encoding = 'utf-8')
    w = file.writelines(f'{a}\n')