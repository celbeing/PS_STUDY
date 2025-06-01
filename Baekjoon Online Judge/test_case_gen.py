import random, math
random.random()
inf = 1 << 31

def euc(a, b):
    while b:
        a, b = b, a % b
    return a

path = r"C:\Users\kimsd\OneDrive\바탕 화면\tc\\"

for tc in range(1, 21):
    n = random.randint(1, 100000)
    W = random.randint(1, 100)
    k = [random.randint(1, W) for _ in range(n)]
    res = 1
    file = open(path + f"{tc}.in", "w+", encoding = 'utf-8')
    w = file.writelines(f'{n} {W}\n')
    line = ''
    box = 0
    for i in range(n):
        line += f'{k[i]} '
        if box + k[i] > W:
            res += 1
            box = k[i]
        else:
            box += k[i]
    w = file.writelines(f'{line.strip()}')

    file = open(path + f'{tc}.out', 'w+', encoding='utf-8')
    w = file.writelines(f'{res}')