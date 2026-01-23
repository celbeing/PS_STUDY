import random
random.random()
check = set()
path = r"C:\Users\kimsd\Documents\GitHub\PS_STUDY\Coalla OJ\기초과정 연습문제\04.두 수의 나눗셈-2\\"

for tc in range(1, 51):
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    a, b = random.randint(0,10000000), random.randint(1,10000)
    while (a, b) in check:
        a, b = random.randint(0,10000000), random.randint(1,10000)
    check.add((a, b))
    w = file.writelines(f'{a}\n{b}\n')

    file = open(path + f'{tc}.out', 'w+', encoding = 'utf-8')
    w = file.writelines(f'{a%b}\n')