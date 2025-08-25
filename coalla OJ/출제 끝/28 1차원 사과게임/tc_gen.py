import random, solution

random.random()
inf = 1 << 31
mod = int(1e9) + 7

path = r"C:\Users\kimsd\OneDrive\바탕 화면\tc\\"

for tc in range(16, 19):
    n = random.randint(400,400)
    a = [random.randint(1, 9) for _ in range(n)]
    b = map(str, a)
    file = open(path + f"{tc}.in", "w+", encoding='utf-8')
    w = file.writelines(f'{n}\n')
    w = file.writelines(' '.join(b))
    file = open(path + f"{tc}.out", "w+", encoding = 'utf-8')
    w = file.writelines(f'{solution.solution(n, a)}')
