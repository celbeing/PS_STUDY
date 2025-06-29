import random
from solution import solution
n = 16

path = r"C:\Users\kimsd\OneDrive\바탕 화면\tc\\"

for tc in range(31, 32):
    while True:
        file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
        now = [0] * n
        for i in range(n):
            for j in range(n):
                t = random.randint(1, 6)
                if t == 1:
                    now[i] |= 1 << j
            line = bin(now[i])[2:]
            if i > 0:
                w = file.writelines(f'\n')
            w = file.writelines(f'{line:0>16}')
        file = open(path + f'{tc}.out', 'w+', encoding='utf-8')
        gen, period = solution(now)
        w = file.writelines(f'{gen} {period}')
        if gen >= 500: break