import random
random.random()
check = set()
path = r"C:\Users\kimsd\Documents\GitHub\PS_STUDY\Coalla OJ\기초과정 연습문제\04.두 수의 나눗셈-2\\"

for tc in range(1, 51):
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    a = random.randint(1, 10000000)
    b = random.randint(1, a)
    while (a, b) in check:
        a = random.randint(1, 10000000)
        b = random.randint(1, a)
    check.add((a, b))
    w = file.writelines(f'{a}\n{b}\n')

    file = open(path + f'{tc}.out', 'w+', encoding = 'utf-8')
    w = file.writelines(f'{a%b}\n')