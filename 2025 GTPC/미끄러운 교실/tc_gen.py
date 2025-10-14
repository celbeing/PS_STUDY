import random
from solution import sol
from solution2 import sol2
path = r'C:\Users\kimsd\OneDrive\Documents\GitHub\PS_STUDY\2025 GTPC\미끄러운 교실\tc\\'

tc = 1
while 1:
    r, c = map(int, input().split())
    if r == c == 0:
        break

    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    w = file.writelines(f'{r} {c}')
    grid = []
    for i in range(r):
        line = input().strip()
        grid.append(list(line))
        w = file.writelines(f'\n{line}')

    file = open(path + f'{tc}.ans', 'w+', encoding='utf-8')
    ans = sol2(r, c, grid)
    w = file.writelines(f'{ans}')

    tc += 1
print('입력이 끝났습니다.')